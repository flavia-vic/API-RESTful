import json

def test_get_items_by_purchase_orders_id(test_client,get_headers,seed_db):
    response = test_client.get('/purchase_orders/{}/items'.format(seed_db['purchase_order'].id),headers=get_headers)
    
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['id'] == seed_db['items'].id
    assert response.json[0]['description'] == seed_db['items'].description
    assert response.json[0]['price'] == seed_db['items'].price
    assert response.json[0]['quantity'] == seed_db['items'].quantity



def test_get_items_by_purchase_orders_not_found(test_client,get_headers):
    id = 999
    response = test_client.get('/purchase_orders/{}/items'.format(id),headers=get_headers)

    assert response.status_code == 200
    assert response.json['message'] == 'Pedido de id {} não encontrado'.format(id)


def test_post_purchase_orders_item(test_client,seed_db,get_headers):
    obj = {
        'description': 'Item teste',
        'price': 10.0, 
        'quantity': 5 
    }

    response = test_client.post(
        '/purchase_orders/{}/items'.format(seed_db['purchase_order'].id),
        data=json.dumps(obj),
        content_type ='application/json',
        headers=get_headers
    )

    assert response.status_code == 200
    assert response.json['id'] is not None
    assert response.json['description'] == obj['description']
    assert response.json['price'] == obj['price']



def test_post_invalid_description(test_client,seed_db,get_headers):
    obj = {
        'price': 10.0,
        'quantity': 5  
    }

    response = test_client.post(
        '/purchase_orders/{}/items'.format(seed_db['purchase_order'].id),
        data=json.dumps(obj),
        content_type ='application/json',
        headers=get_headers
    )

    assert response.status_code == 400
    assert response.json['message']['description'] == 'Informe uma descrição válida'

def test_post_invalid_price(test_client,seed_db,get_headers):
    obj = {
        'description': 'Item teste',
        'quantity': 10
    }

    response = test_client.post(
        '/purchase_orders/{}/items'.format(seed_db['purchase_order'].id),
        data=json.dumps(obj),
        content_type ='application/json',
        headers=get_headers
    )

    assert response.status_code == 400
    assert response.json['message']['price'] == 'Informe um preço válido'


def test_post_purchase_order_invalid(test_client,get_headers):
    id = 999999
    obj = {
        'description': 'Item teste',
        'price':10.0,
        'quantity': 5
    }
        
    response = test_client.post(
        '/purchase_orders/{}/items'.format(id),
        data=json.dumps(obj),
        content_type ='application/json',
        headers=get_headers
    )

    assert response.json['message'] == 'Purchase Order {} não encontrado'.format(id)


def test_post_purchase_order_item_invalid_quantity(test_client, seed_db,get_headers):
    obj = {
        'description': 'Item teste',
        'price': 10.0,
        'quantity': 201
    }

    response = test_client.post(
        '/purchase_orders/{}/items'.format(seed_db['purchase_order'].id),
        data=json.dumps(obj),
        content_type='application/json',
        headers=get_headers
    )

    assert response.status_code == 400
    assert response.json['message'] == 'Você somente pode adicionar mais 20 itens'


def test_post_invalid_quantity(test_client,seed_db,get_headers):
    obj = {
        'price': 10.0,
        'description': 'Teste invalid quantity'
    }

    response = test_client.post(
        '/purchase_orders/{}/items'.format(seed_db['purchase_order'].id),
        data=json.dumps(obj),
        content_type='application/json',
        headers=get_headers
    )

    assert response.status_code == 400
    assert response.json['message']['quantity'] == 'Informe uma quantidade válida'


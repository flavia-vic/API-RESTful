import json


def test_get_purchase_orders(test_client):
    response = test_client.get('/purchase_orders')

    assert response.status_code == 200
    assert response.json[0]['id']  == 1
    assert response.json[0]['description'] == 'Purchase Order id 1'
    assert len(response.json[0]['items']) == 1
    assert response.json[0]['items'][0]['id'] == 1


def test_post_purchase_orders(test_client):
    obj = {'id':2,'description':'Purchase Order Id 2'}

    response = test_client.post(
        '/purchase_orders',
        data =json.dumps(obj),
        content_type = 'application/json'
    )

    assert response.status_code == 200
    assert response.json['id'] == obj['id']
    assert response.json['description'] == obj['description']
    assert response.json['items'] == []
    


    
###### Testando cenarios de falha 
def test_post_empty_id(test_client):
        response = test_client.post(
            '/purchase_orders', 
            data =json.dumps({'description': 'descrição'}),
            content_type = 'application/json'
        )           

        assert response.status_code == 400
        assert response.json['message']['id'] == 'informe um id válido'   


    
def test_post_empty_description(test_client):
        response = test_client.post(
            '/purchase_orders', 
            data =json.dumps({'id': 2}),
            content_type = 'application/json'
        )           

        assert response.status_code == 400
        assert response.json['message']['description'] == 'informe uma descrição válida' 



def test_get_purchase_order_by_id(test_client):
          response = test_client.get('purchase_orders/1')

          assert response.status_code == 200
          assert response.json['id'] == 1
          assert response.json['description'] == 'Purchase Order id 1'



def test_get_items_by_purchase_order_id_not_found(test_client):
        id = 9999
        response = test_client.get('/purchase_orders/{}/items'.format(id))

        assert response.status_code == 200
        assert response.json['message']=='Pedido de id {} não encontrado'.format(id)


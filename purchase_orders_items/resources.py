from flask_restful import Resource, reqparse
from .model import PurchaseOrdersItemsModel
from purchase_orders.model import PurchaseOrderModel
from flasgger import swag_from
from flask import jsonify



class PurchaseOrdersItems(Resource):
    parser = reqparse.RequestParser()
    
    parser.add_argument(
        'description',
        type=str,
        required = True,
        help = 'Informe uma descrição válida'
    )
    parser.add_argument(
        'price',
        type = float,
        required = True,
        help = 'Informe um preço válido'
    )

    @swag_from('../docs/get_item_by_id.yml')
    def get(self,id):
        purchase_orders_items = PurchaseOrdersItemsModel.find_by_id_purchase_order_id(id)

        return [p.as_dict() for p in purchase_orders_items]


    @swag_from('../docs/post_item.yml')
    def post(self,id):
        purchase_order = PurchaseOrderModel.find_by_id(id)
        if purchase_order:
            data = PurchaseOrdersItems.parser.parse_args()
            data['purchase_order_id'] = id

            purchase_orders_item = PurchaseOrdersItemsModel(**data)
            purchase_orders_item.save()

            return purchase_orders_item.as_dict()


        return jsonify({'message':'Purchase Order {} não encontrado'.format(id)})
            


    


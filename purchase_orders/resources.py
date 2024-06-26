from flask_restful import Resource, reqparse
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from .service import PurchaseOrderService
from flask import jsonify

class PurchaseOrders(Resource):
    __service__= PurchaseOrderService()
    method_decorators = [jwt_required()] 
    parser = reqparse.RequestParser()
    parser.add_argument(
        'description',
        type = str,
        required= True,
        help = 'informe uma descrição válida'
    )
    parser.add_argument(
        'quantity',
        type = int,
        required = True,
        help = 'informe uma quantidade'
        )

    @swag_from('../docs/get_purchases.yml')
    def get(self):
        return self.__service__.find_all()
        
    
    @swag_from('../docs/create_purchase.yml')
    def post(self):
        data = PurchaseOrders.parser.parse_args()
        return self.__service__.create(**data)
 

class purchaseOrdersById(Resource):
    __service__ = PurchaseOrderService()

    @swag_from('../docs/get_purchase_by_id.yml')
    def get(self,id):
       return self.__service__.find_by_id(id)

        
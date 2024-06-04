from flask import Flask
from flask_restful import Api
from db import db
from flasgger import Swagger


from purchase_orders.resources import PurchaseOrders, purchaseOrdersById
from purchase_orders_items.resources import PurchaseOrdersItems


def create_app(env):
        
    app = Flask (__name__)
    api = Api(app)
    swagger = Swagger(app)

    database = 'Teste'
    if env == 'testing':
        database = 'Teste'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://pi:raspberry@192.168.1.10/{}'.format(database)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    api.add_resource(PurchaseOrders,'/purchase_orders')
    api.add_resource(purchaseOrdersById, '/purchase_orders/<int:id>')
    api.add_resource(PurchaseOrdersItems, '/purchase_orders/<int:id>/items')

    @app.before_request 
    def create_tables():
        db.create_all()
    return app
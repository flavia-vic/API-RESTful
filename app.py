import os
from flask import Flask
from flask_restful import Api
from db import db
from flasgger import Swagger
from flask_migrate import Migrate
from flask_JWT_estended import JWTManager



from purchase_orders.resources import PurchaseOrders, purchaseOrdersById
from purchase_orders_items.resources import PurchaseOrdersItems


def create_app():
        
    app = Flask (__name__)
    api = Api(app)
    swagger = Swagger(app)


    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']

    db.init_app(app)

    Migrate(app,db)
    JWTManager(app)

    api.add_resource(PurchaseOrders,'/purchase_orders')
    api.add_resource(purchaseOrdersById, '/purchase_orders/<int:id>')
    api.add_resource(PurchaseOrdersItems, '/purchase_orders/<int:id>/items')

    @app.before_request 
    def create_tables():
        db.create_all()
    return app
import os
from flask import Flask
from flask_restful import Api
from db import db
from flasgger import Swagger
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager



from purchase_orders.resources import PurchaseOrders, purchaseOrdersById
from purchase_orders_items.resources import PurchaseOrdersItems
from users.resources import CreateUser, Userlogin

def create_app():      
    app = Flask (__name__)
    api = Api(app)

    swagger = Swagger(app)


    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']

    db.init_app(app)

    Migrate(app,db)
    jwt = JWTManager(app)


    api.add_resource(PurchaseOrders,'/purchase_orders')
    api.add_resource(purchaseOrdersById, '/purchase_orders/<int:id>')
    api.add_resource(PurchaseOrdersItems, '/purchase_orders/<int:id>/items')
    api.add_resource(CreateUser,'/users')
    api.add_resource(Userlogin,'/login')

    @jwt.invalid_token_loader
    def invalid_jwt(error):
        return (
            {"message": "Token de acesso inválido"},
            401
        )

    @jwt.unauthorized_loader
    def unauthorized_jwt(error):
        return (
            {"message": "Sem autorização, por favor informe um token válido"},
            401
        )

    @app.before_request 
    def create_tables():
        db.create_all()

    return app

if __name__ == '__main__':
    app.run(debug=True)
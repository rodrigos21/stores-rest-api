import os
import re

from flask import Flask
from security import authenticate, identity
from flask_restful import Api
from flask_jwt import JWT

from db import db

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "rodri"

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL','postgresql://srfnxnnrurbkdl:36cd7f5d7a7387a9fb10974c41a0f71e1c511b8499ddda3d8b4545acd5756c6b@ec2-3-214-190-189.compute-1.amazonaws.com:5432/de4n5fnp593i6n','sqlite:///data.db')

""" uri = os.getenv("DATABASE_URL","sql:///data.db")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri` """

api = Api(app)




jwt= JWT(app, authenticate, identity)   #/auth

api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item,"/item/<string:name>")  
api.add_resource(ItemList, "/items")
api.add_resource(StoreList, "/stores")

api.add_resource(UserRegister, "/register")


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)

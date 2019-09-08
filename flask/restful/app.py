import logging
from flask import Flask
from flask_restful import Api

log = logging.getLogger("app.restful")

from resources import Login
from resources import Users
from data import UserData

data = UserData()
app = Flask(__name__)
api = Api(app)

api.add_resource(Login, "/login", 
                 resource_class_kwargs={"user_data":data})
api.add_resource(Users, "/users",
                 resource_class_kwargs={"user_data":data})


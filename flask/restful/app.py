import logging
from flask import Flask
from flask_restful import Api

log = logging.getLogger("app.restful")

from resources import User
from data import UserData

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/user',
                 resource_class_kwargs={'user_data':UserData()})

from flask import request, jsonify
from flask_restful import Resource

class Users(Resource):
    def __init__(self, **kwargs):
        self.user_data = kwargs["user_data"]

    def get(self):
        return jsonify(self.user_data.users_list())
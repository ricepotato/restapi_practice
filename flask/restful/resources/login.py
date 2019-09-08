from flask import request, jsonify
from flask_restful import Resource

class Login(Resource):
    def __init__(self, **kwargs):
        self.user_data = kwargs["user_data"]

    def post(self):
        id = request.form["id"]
        password = request.form["password"]
        key = self.user_data.login(id, password)
        if key is None:
            return jsonify({"msg":"user not found."})
        else:
            return jsonify({"msg":"login success.", "user_key":key})
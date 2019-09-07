from flask_restful import Resource

class Login(Resource):
    def __init__(self, **kwargs):
        self.user_data = kwargs["user_data"]

    def post(self):
        pass
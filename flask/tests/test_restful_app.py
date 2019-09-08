#-*- coding: utf-8 -*-
import os
import sys
import json
import unittest
import logging

from flask import Flask, jsonify
from flask_restful import Resource, Api

log = logging.getLogger("app.tests.restful")
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

cur_path = os.path.dirname(__file__)
base_path = os.path.join(cur_path, "..")
sys.path.append(base_path)

from restful.data import UserData
from restful.resources import Login
from restful.resources import Users

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        api = Api(app)
        data = UserData()
        api.add_resource(Login, "/login", 
                         resource_class_kwargs={"user_data":data})
        api.add_resource(Users, "/users",
                         resource_class_kwargs={"user_data":data})
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_restful_app_login(self):
        res = self.app.post("/login", data={"id":"sukjun.sagong", 
                                            "password":"password"})
        res_json = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_json["user_key"], 1)
        self.assertEqual(res_json["msg"], "login success.")

        res = self.app.post("/login", data={"id":"sukjun.sagong", 
                                            "password":"invalid_password"})
        self.assertEqual(res.status_code, 200)
        res_json = json.loads(res.data)
        self.assertEqual(res_json["msg"], "user not found.")

        res = self.app.post("/login", data={"id":"id_not_found"})
        self.assertEqual(res.status_code, 400)

    def test_restful_app_users(self):
        res = self.app.get("/users")
        self.assertEqual(res.status_code, 200)
        res_json = json.loads(res.data)
        self.assertEqual(len(res_json), 2)
        

if __name__ == "__main__":
    unittest.main()

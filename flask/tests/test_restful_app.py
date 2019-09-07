#-*- coding: utf-8 -*-
import os
import sys
import json
import unittest

try:
    from flask import Flask, jsonify
    from flask_restful import Resource, Api
except ImportError as e:
    log.error("import error. install flask 'pip install flask'")

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        api = Api(app)
        rck = {"st_data":st_data}
        api.add_resource(Stock, "/stock", "/stock/<string:market>", 
                         resource_class_kwargs=rck)
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_restful_app(self):
        pass

if __name__ == "__main__":
    unittest.main()

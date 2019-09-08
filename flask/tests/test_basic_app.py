#-*- coding: utf-8 -*-
import os
import sys
import json
import unittest

cur_path = os.path.dirname(__file__)
base_path = os.path.join(cur_path, "..")
sys.path.append(base_path)

from basic.app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        #app = Flask(__name__)
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_basic_app_index(self):
        res = self.app.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data.decode("utf-8"), "Hello World!")

    def test_basic_app_rec(self):
        res = self.app.get("/rec")
        self.assertEqual(res.status_code, 200)
        res_json = json.loads(res.data)
        self.assertEqual(res_json["msg"], "hello world!")

    def test_basic_not_found(self):
        res = self.app.get("/not_found")
        self.assertEqual(res.status_code, 404)

    def test_basic_error(self):
        res = self.app.get("/error")
        self.assertEqual(res.status_code, 500)

if __name__ == "__main__":
    unittest.main()

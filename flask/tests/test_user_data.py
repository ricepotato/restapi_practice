#-*- coding: utf-8 -*-
import os
import sys
import json
import unittest

cur_path = os.path.dirname(__file__)
base_path = os.path.join(cur_path, "..")
sys.path.append(base_path)

from restful.data import UserData

class UserDataTestCase(unittest.TestCase):
    def setUp(self):
        self.user_data = UserData()

    def tearDown(self):
        pass

    def test_user_data(self):
        pass

if __name__ == "__main__":
    unittest.main()

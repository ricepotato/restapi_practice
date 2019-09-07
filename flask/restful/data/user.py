import logging

log = logging.getLogger("app.restful.resources.user")

class UserData:
    def __init__(self):
        self.users_dict = {
            1:{
                "id":"sukjun.sagong",
                "name":"sukjun.sagong",
                "phone":"010-1234-5678",
                "password":"password"
                },
            2:{
                "id":"ricepotato",
                "name":"ricepotato",
                "phone":"010-4567-8901",
                "password":"password"
            }
        }

    def login(self, id: str, password: str) -> dict:
        """ user login """
        for key, val in self.users_dict.items():
        if val["id"] == id and val["password"] == password:
            log.info("login success user_key=%s", str(key))
            return key
        else:
            return None

    def create_user(self, user: dict) -> int:
        new_id = self._get_id()
        new_user = {
            "id":user["id"], "name":user["name"],
            "phone":user["phone"], "password":user["password"]
        }
        self.users_dict[new_id] = new_user
        return new_id

    def users_list(self) -> list:
        return list(map(lambda user_id: self.users_dict[user_id], 
                        self.users_dict))

    def user(self, id: int) -> dict:
        return self.users_dict[id]

    def _get_id(self):
        id = 1
        while True:
            if self.users_dict.get(id, None):
                id += 1
            else:
                return id

import logging
from flask import Flask, jsonify, request

log = logging.getLogger("app.restapi.flask.method")
log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)

app = Flask(__name__)

users_dict = {
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

@app.errorhandler(404)
def page_not_found(error):
    #return render_template('page_not_found.html'), 404
    return jsonify({"msg":"page not found"})

def get_id(users_dict):
    id = 1
    while True:
        if users_dict.get(id, None):
            id += 1
        else:
            return id

@app.route("/users", methods=["GET"])
def users():
    res_list = list(map(lambda user_id: users_dict[user_id], users_dict))
    return jsonify(res_list)

@app.route("/user/<int:id>", methods=["GET", "DELETE", "PATCH", "PUT"])
def user(id):
    if request.method == 'GET':
        return jsonify(users_dict[id])
    if request.method == "DELETE":
        del users_dict[id]
        return jsonify({"success":True})
    if request.method == "PATCH":
        return jsonify({"success":True})
    if request.method == "PUT":
        return jsonify({"success":True})


@app.route("/login", methods=["POST"])
def login():
    id = request.form["id"]
    password = request.form["password"]
    for key, val in users_dict.items():
        if val["id"] == id and val["password"] == password:
            log.info("login success user_key=%s", str(key))
            return jsonify({"msg":"login success.", "user_key":key})
    else:
        return jsonify({"msg":"user not found."})

@app.route("/user", methods=["POST"])
def user_register():
    new_id = get_id(users_dict)
    new_user = {
        "id":request.form["id"], "name":request.form["name"],
        "phone":request.form["phone"], "password":request.form["password"]
    }
    users_dict[new_id] = new_user
    log.info("user register name=%s", new_user)
    return jsonify({"success":True, "user_key":new_id})

def main():
    app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ == '__main__':
    main()

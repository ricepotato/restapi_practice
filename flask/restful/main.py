import logging
from app import app

log = logging.getLogger("app.restapi.flask.main")
log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)

def main():
    app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ == '__main__':
    main()

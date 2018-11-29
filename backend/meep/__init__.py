import os

from flask import Flask, jsonify
from flask_cors import CORS

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    CORS(app)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    @app.route('/api/register', methods=["POST"])
    def register():
        return jsonify("Hallo");

    @app.route('/api/login', methods=["POST"])
    def login():
        return jsonify("aayy");

    @app.route('/helloWorld')
    def helloWorld():
        test = [{
            'name': 'Alex',
            'major': "C.S."
        },
        {
            'name': 'Jeter',
            'major': "C.S."
        }]
        return jsonify(test);

    return app

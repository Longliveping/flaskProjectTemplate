from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from config import config
from flask_sqlalchemy import SignallingSession
import logging

db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()

def create_app(config_name):
    logging.basicConfig(filename="app.log", level=logging.DEBUG)
    print(f' * Running under config: {config_name}')
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
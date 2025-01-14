from flask import Flask, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
# from logging import basicConfig, DEBUG, getLogger, StreamHandler
# from os import path

db = SQLAlchemy()
login_manager = LoginManager()

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)

def register_blueprints(app):
    for module_name in ('base','admin'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()
        from app.admin.models import  Admin
        instance = db.session.query(Admin).filter_by(email='skiran252@gmail.com').first()
        if instance:
            pass
        else:
            admin=Admin("saikiran", "skiran252@gmail.com", 'gonugunta')
            db.session.add(admin)
            db.session.commit()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def create_app(config):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    return app

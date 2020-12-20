# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db  = SQLAlchemy()


def create_app(config_type): #dev, Test, Prod

    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')

    app.config.from_pyfile(configuration)  # load configuration file from python

    db.init_app(app)   # initiate the flask app for database 

    from app.catalog import main

    app.register_blueprint(main) # register blueprint from flask application

    return app


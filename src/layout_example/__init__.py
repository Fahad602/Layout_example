from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from datetime import datetime
from layout_example.api import routes

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Abcde.123@localhost:5432/blogs'
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    app.register_blueprint(routes.app)

    return app

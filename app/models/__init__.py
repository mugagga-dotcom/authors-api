#The models defines your data structure.
#The __init__.py turns ypour app into a python package and its usually where the flask app is created.
from flask import Flask
from app.extensions import db, migrate

def create_app():
    app = Flask(__name__)

    # config
    app.config.from_object('config.Config')

    # extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # IMPORTANT: import models so Flask-Migrate can see them
    from app.models.users import User
    from app.models.companies import Company
    from app.models.books import Book

    # routes
    @app.route("/")
    def home():
        return "Authors API Project Setup 1"

    return app


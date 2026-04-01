# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager
# from .config import Config
# db = SQLAlchemy()
# jwt = JWTManager()
# def create_app():
# app = Flask(__name__)
# app.config.from_object(Config)
# db.init_app(app)
# jwt.init_app(app)
# # Register blueprints (routes) — uncomment as you build each session
# from .routes.authors import authors_bp
# from .routes.books import books_bp
# from .routes.auth import auth_bp
# app.register_blueprint(authors_bp)
# app.register_blueprint(books_bp)
# app.register_blueprint(auth_bp)
# return app
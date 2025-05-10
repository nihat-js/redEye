from flask import Flask
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from datetime import datetime

# MongoDB instance yaradırıq
mongo = PyMongo()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # MongoDB konfiqurasiyası
    app.config["MONGO_URI"] = "mongodb://root:nihatnihat@localhost:27018/redeye?authSource=admin"
    app.config["JWT_SECRET_KEY"] = "super-a910ka9r10"
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    app.config["JWT_ACCESS_COOKIE_PATH"] = "/"  # bütün endpoint-lərə aid olsun
    app.config["JWT_COOKIE_SECURE"] = False  # HTTPS-də True elə
    app.config["JWT_COOKIE_CSRF_PROTECT"] = False

    @app.context_processor
    def utility_processor():
        return {
            'datetime': datetime
        }


    # MongoDB-ni initialize edirik
    mongo.init_app(app)
    jwt.init_app(app)

    
    # Blueprint-ləri qeydiyyatdan keçiririk
    from app.auth import authBlueprint
    app.register_blueprint(authBlueprint)

    from app.portal import portalBlueprint
    app.register_blueprint(portalBlueprint)

    from app.api import apiBlueprint
    app.register_blueprint(apiBlueprint)

    from app.home import homeBlueprint
    app.register_blueprint(homeBlueprint)
    
    return app
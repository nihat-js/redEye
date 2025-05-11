from bson import ObjectId
from flask import Flask, g
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_identity
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
    app.config['UPLOAD_FOLDER'] = 'uploads'

    @app.context_processor
    def utility_processor():
        return {
            'datetime': datetime
        }


    # MongoDB-ni initialize edirik
    mongo.init_app(app)
    jwt.init_app(app)

    @app.before_request
    def before_request():
        try:
            verify_jwt_in_request(optional=True)
            id= get_jwt_identity()
            print("id is " + id)
            if id:
                user = mongo.db.users.find_one({"_id":  ObjectId(id) })
                print("Logged in user " + user.get("username"))
                if user:
                    g.current_user = user
                else:
                    g.current_user = None
            else:
                g.current_user = None
        except Exception:
            g.current_user = None

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
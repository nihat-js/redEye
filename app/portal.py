from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import mongo

portalBlueprint = Blueprint('portalBlueprint', __name__)


@portalBlueprint.get("/portal")
@jwt_required()
def portal():
    username =  get_jwt_identity()
    user = mongo.db.users.find_one({"username": username})

    return render_template("portal/index.html",current_user=user,user=username)

@portalBlueprint.get("/portal/enumeration")
@jwt_required()
def enumerate():
    username =  get_jwt_identity()
    user = mongo.db.users.find_one({"username": username})
    return render_template("portal/enumeration.html",current_user=user,user=username)


@portalBlueprint.get("/portal/exploitation")
@jwt_required()
def exploit():
    username =  get_jwt_identity()
    user = mongo.db.users.find_one({"username": username})
    return render_template("portal/exploitation.html",current_user=user,user=username)


@portalBlueprint.get("/portal/activeDirectory")
@jwt_required()
def ad():
    username =  get_jwt_identity()
    user = mongo.db.users.find_one({"username": username})
    return render_template("portal/activeDirectory.html",current_user=user,user=username)


@portalBlueprint.get("/portal/privilegeEscalation")
@jwt_required()
def privilege():
    username =  get_jwt_identity()
    user = mongo.db.users.find_one({"username": username})
    return render_template("portal/privilegeEscalation.html",current_user=user,user=username)

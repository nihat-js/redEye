import secrets

from flask import Blueprint, render_template, request, redirect, make_response
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, get_jwt_identity

from app import mongo
authBlueprint = Blueprint('auth', __name__)


users = [
    {"username": "root", "password": "yalicapkini", "apiToken": secrets.token_hex()},
    {"username": "enumerate", "password": "enumerateWho", "apiToken": secrets.token_hex()},
    {"username": "exploit", "password": "exploitMe", "apiToken": secrets.token_hex()},
    {"username": "privesc", "password": "privEscThen", "apiToken": secrets.token_hex()},
    {"username": "ad", "password": "ihatead", "apiToken": secrets.token_hex()},
]




@authBlueprint.get("/login")
def login():
    return render_template('auth/login.html')


@authBlueprint.post("/login")
def loginPost():
    username = request.form["username"]
    password = request.form["password"]

    user = mongo.db.users.find_one({"username": username})
    if user and user["password"] == password:
        access_token = create_access_token(identity=username)
        response = make_response(redirect("/portal"))
        set_access_cookies(response, access_token)
        return response

    else:
        return render_template("auth/login.html", error="Invalid username or password")



@authBlueprint.get("/logout")
def logout():
    response = make_response(redirect("/login"))
    response.set_cookie("access_token", "", expires=0)
    return redirect("/")


##################################################################################
###                    For Developers only ES                                 ####
@authBlueprint.get("/users")
def users():
    users = mongo.db.users.find()
    return list(users)


@authBlueprint.get("/resetUsers/")
def populateUsers():


    try:
        mongo.db.users.drop()
        result = mongo.db.users.insert_many(users)
        return f"Users created: {len(result.inserted_ids)}"
    except Exception as e:
        return f"An error occurred: {e}"



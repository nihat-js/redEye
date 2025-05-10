from flask import Blueprint, jsonify, request
from app import mongo

apiBlueprint = Blueprint("api", __name__)

@apiBlueprint.route("/api", methods=["GET"])
def api_info():
    return jsonify({"message": "Come on!. Our site is super-secure. Get off my lawn! "})

@apiBlueprint.route("/api/incidents/<token>", methods=["POST"])
def exfiltrate(token):
    print(token)
    user = mongo.db.users.find_one({"apiToken": token})

    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    data["owner"] = user["username"]
    mongo.db.incidents.insert_one(data)
    return jsonify({"message": "Data exfiltrated successfully"}), 200

from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)


@api_bp.route("/data")
def get_data():
    data = {"message": "This is the data from the backend!"}
    return jsonify(data)

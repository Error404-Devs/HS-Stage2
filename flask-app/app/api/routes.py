from flask import jsonify
from . import api_bp


@api_bp.route("/data")
def get_data():
    data = {"message": "This is the data from the backend!"}
    return jsonify(data)

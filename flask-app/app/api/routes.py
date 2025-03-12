from flask import jsonify, request
from . import api_bp
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import threading
import time

from app.database.database import db
from app.database.models.users import User

latest_rfid = {"id": None, "text": None}  # Store the last read RFID data

def rfid_reader():
    global latest_rfid
    reader = SimpleMFRC522()
    while True:
        try:
            print("Waiting for RFID scan...")
            rfid_id, text = reader.read()
            print(f"Scanned RFID: {rfid_id}, Data: {text}")
            latest_rfid = {"id": rfid_id, "text": text}  # Store the latest scan
            time.sleep(2)  # Prevent repeated scanning
        except Exception as e:
            print(f"RFID Read Error: {e}")
        finally:
            GPIO.cleanup()
            
# Start RFID reading in a separate thread
rfid_thread = threading.Thread(target=rfid_reader, daemon=True)
rfid_thread.start()

@api_bp.route("/rfid/latest")
def get_latest_rfid():
    return jsonify(latest_rfid)


# User Endpoints
@api_bp.route("/users", methods=["GET"])
def get_users():
    users = db.get_all_users()
    return jsonify(users)

@api_bp.route("/users", methods=["POST"])
def create_user():
    data = request.json
    new_user = db.insert_user(
        user_id=data.get("user_id"),
        username=data.get("username"),
        password=data.get("password"),
        role=data.get("role")
    )
    return jsonify(new_user)

@api_bp.route("/users/<string:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json # (4, {"username": "NEWUSERNAME"})
    updated_user = db.update_user(user_id, updated_fields=data)
    return jsonify(updated_user)

@api_bp.route("/users/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    result = db.delete_user(user_id)   
    return jsonify(result)



# Tag Endpoints
@api_bp.route("/tags", methods=["GET"])
def get_tags():
    tags = db.get_all_tags()
    return jsonify(tags)

@api_bp.route("/tags", methods=["POST"])
def create_tag():
    data = request.json
    tag_id = data.get("id")
    name = data.get("name")
    user_data = data.get("data")
    
    users = [User(**user) for user in user_data]

    new_tag = db.insert_tag(
        tag_id=tag_id,
        name=name,
        users=users
    )

    if new_tag:
        return jsonify(new_tag), 201
    return jsonify({"error": "Error creating tag"}), 400

@api_bp.route("/tags/<string:tag_id>", methods=["PUT"])
def update_tag(tag_id):
    data = request.json
    updated_tag = db.update_tag(tag_id, updated_fields=data)
    if updated_tag:
        return jsonify(updated_tag), 200
    return jsonify({"error": "Tag not found or validation failed"}), 404

@api_bp.route("/tags/<string:tag_id>", methods=["DELETE"])
def delete_tag(tag_id):
    result = db.delete_tag(tag_id)
    if result[0]:
        return jsonify({"message": result[1]}), 200
    return jsonify({"error": result[1]}), 404
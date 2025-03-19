from flask import jsonify, request
from . import api_bp
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
from pydantic import BaseModel
import RPi.GPIO as GPIO
from app.database.database import db
from app.database.models.users import User
from app.database.utils.logs import insert_log
import uuid

<<<<<<< HEAD
# import Adafruit_SSD1306
# from PIL import Image, ImageDraw, ImageFont
=======
from app.database.database import db
from app.database.models.users import User

latest_rfid = {"id": None, "text": None}  # Store the last read RFID data
>>>>>>> upstream/main

# LEDS LIGHT

LED_ONE = 27
LED_TWO = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_ONE, GPIO.OUT)
GPIO.setup(LED_TWO, GPIO.OUT)


@api_bp.route('/led/1/on', methods=['GET'])
def led_1_on():
    GPIO.output(LED_ONE, GPIO.HIGH)
    GPIO.output(LED_TWO, GPIO.LOW)
    data_returned = {
        "data": {
            "id": "1",
            "led": "1"
        }
    }
    insert_log(log_id=str(uuid.uuid4()), message= "LED ONE TURN ON!", data=data_returned)
    GPIO.cleanup
    return jsonify({"status": "success", "message": "LED 1 turned on, LED 2 turned off"}), 200

@api_bp.route('/led/2/on', methods=['GET'])
def led_2_on():
    GPIO.output(LED_ONE, GPIO.LOW)
    GPIO.output(LED_TWO, GPIO.HIGH)
    data_returned = {
        "data": {
            "id": "1",
            "led": "2"
        }
    }
    insert_log(log_id=str(uuid.uuid4()), message= "LED TWO TURN ON!", data=data_returned)
    GPIO.cleanup
    return jsonify({"status": "success", "message": "LED 1 turned off, LED 2 turned on"}), 200

@api_bp.route('/led/off', methods=['GET'])
def all_off():
    GPIO.output(LED_ONE, GPIO.LOW)
    GPIO.output(LED_TWO, GPIO.LOW)
    data_returned = {
        "data": {
            "id": "1",
            "led": "off"
        }
    }
    insert_log(log_id=str(uuid.uuid4()), message= "LED TURNED OFF!", data=data_returned)
    GPIO.cleanup
    return jsonify({"status": "success", "message": "LED 1 turned off, LED 2 turned on"}), 200



# Global variable to store the RFID scan result
scanned_rfid = None

def read_rfid_loop():
    global scanned_rfid
    reader = SimpleMFRC522()
<<<<<<< HEAD

=======
>>>>>>> upstream/main
    while True:
        try:
            print("Waiting for RFID scan...")
            tag_id, text = reader.read()
            scanned_rfid = {"id": tag_id, "name": text, "data": "Something"}
            print(f"✅ Scanned RFID: {scanned_rfid}")
            time.sleep(1)
            return scanned_rfid
        except Exception as e:
<<<<<<< HEAD
            print(f"❌ Error while reading RFID: {e}")
            time.sleep(2)  # Avoid busy loop on failure

@api_bp.route('/wait_for_rfid', methods=['GET'])
def wait_for_rfid():
    print("Waiting for RFID scan...")
    read_rfid_loop()

    log_id = str(uuid.uuid4())
    print(log_id, scanned_rfid, "Scanned RFID!")
    object, error = db.insert_log(log_id=log_id, tag=scanned_rfid, message="Scanned RFID!")
    if not error:
        return jsonify({"status": "success", "object": object}), 200
    else:
        return jsonify({"status": "failed"}, error), 200


@api_bp.route('/get_logs', methods=['GET'])
def get_logs():
    return db.get_all_logs()




# # # MESSAGE DISPLAY

# # Initialize the display (use the correct I2C address if needed)
# display = Adafruit_SSD1306.SSD1306_128_64(rst=None)
# display.begin()
# display.clear()
# display.display()

# # Create a blank image for drawing
# image = Image.new('1', (display.width, display.height))
# draw = ImageDraw.Draw(image)

# # Load a default font
# font = ImageFont.load_default()

# # Draw some text on the image
# draw.text((0, 0), 'Hello, Raspberry Pi!', font=font, fill=255)

# # Display the image on the screen
# display.image(image)
# display.display()

# # Wait for a few seconds before clearing the screen
# time.sleep(5)
# display.clear()
# display.display()


#LOGIN 

class Login(BaseModel):
    username: str
    password: str


@api_bp.route("/login", methods=["POST"])
def login():
    users = db.get_all_users()
    data = request.json
    for user in users:
        if str(user.get("username")) == str(data.get("username")) and str(user.get("password")) == str(data.get("password")):
            return jsonify(user), 200
    return "Login failed", 400

@api_bp.route("/check_tag", methods=["POST"])
def check_tag():
    tags = db.get_all_tags()
    data = request.json
    for tag in tags:
        if tag.get("data").get("id") == data.get("id"):
            read_rfid_loop()
            print(tag)
            insert_log(log_id=str(uuid.uuid4()), message= "RFID SCANNED SUCCESSFULLY", data=tag)
            
            if str(scanned_rfid.get("id")) == str(tag.get("id")):
                if str(tag.get("id")) == "1044211108658":
                    led_1_on()
                elif str(tag.get("id")) == "358152211892":
                    led_2_on()
                else:
                    all_off()
                return data, 200 
    data_returned = {
        "data": {
            "id": "0",
            "error": "Wrong tag"
        }
    }
    insert_log(log_id=str(uuid.uuid4()), message= "RFID SCANNED FAILED", data=data_returned)
    all_off()
    return jsonify({"message":"Wrong tag"}), 400

=======
            print(f"RFID Read Error: {e}")
        finally:
            GPIO.cleanup()
            
# Start RFID reading in a separate thread
rfid_thread = threading.Thread(target=rfid_reader, daemon=True)
rfid_thread.start()

@api_bp.route("/rfid/latest")
def get_latest_rfid():
    return jsonify(latest_rfid)


>>>>>>> upstream/main
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



<<<<<<< HEAD



=======
>>>>>>> upstream/main
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
from flask import jsonify
from . import api_bp
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import threading
import time

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

import requests
from flask import render_template
from . import frontend_bp  # Import the frontend_bp blueprint
import psutil
import os

def get_cpu_info():
    cpu_info = {
        "architecture": os.uname().machine,
        "cpu_model": "Broadcom BCM2837" if "arm" in os.uname().machine.lower() else "Unknown",
        "cpu_frequency": f"{psutil.cpu_freq().current:.2f} MHz",
        "cpu_cores": psutil.cpu_count(logical=False),
        "logical_processors": psutil.cpu_count(logical=True),
        "cpu_usage": f"{psutil.cpu_percent(interval=1)}%",
        "temperature": f"{get_cpu_temperature()}°C"
    }
    return cpu_info

def get_cpu_temperature():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
            temp = int(file.read()) / 1000  # Convert to °C
            return round(temp, 1)
    except FileNotFoundError:
        return "N/A"

@frontend_bp.route("/")
def home():
    cpu_info = get_cpu_info()

    # Fetch RFID data from backend
    try:
        response = requests.get("http://127.0.0.1:5000/api/rfid/latest")
        rfid_data = response.json()
    except:
        rfid_data = {"id": "N/A", "text": "No data available"}

    return render_template("index.html", cpu_info=cpu_info, rfid_data=rfid_data)

@frontend_bp.route("/login", methods=["GET", "POST"])
def login():
    # if request.method == "POST":
    #     username = request.form.get("username")
    #     password = request.form.get("password")

    #     # Make a request to your API backend for authentication
    #     response = requests.post(
    #         "http://127.0.0.1:5000/api/login",
    #         json={"username": username, "password": password},
    #     )

    #     if response.status_code == 200:
    #         session["user"] = username  # Store the user session
    #         flash("Login successful!", "success")
    #         return redirect(
    #             url_for("frontend_bp.index")
    #         )  # Redirect to home page or dashboard
    #     else:
    #         flash("Invalid credentials. Please try again.", "danger")

    return render_template("login.html")


@frontend_bp.route("/signup", methods=["GET", "POST"])
def signup():

    return render_template("signup.html")

@frontend_bp.route("/user", methods=["GET", "POST"])
def user():

    return render_template("user.html")

@frontend_bp.route("/admin", methods=["GET", "POST"])
def admin():

    return render_template("admin.html")


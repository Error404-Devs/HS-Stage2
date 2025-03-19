import requests
from flask import render_template, request
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

        response_users = requests.get("http://127.0.0.1:5000/api/users")
        print(response_users.json())
        users = response.json()
    except:
        rfid_data = {"id": "N/A", "text": "No data available"}
    # print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{users}")
    return render_template("index.html", cpu_info=cpu_info, rfid_data=rfid_data) #, users=users)

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

@frontend_bp.route("/user", methods=["GET"])
<<<<<<< HEAD
def user_page():
    username = request.args.get('username', 'Guest')  # Get username from URL query params
    return render_template('user.html', user=username)  # Pass user to template
=======
def user():

    return render_template("user.html")
>>>>>>> upstream/main

@frontend_bp.route("/admin", methods=["GET", "POST"])
def admin():
    
<<<<<<< HEAD
    return render_template("admin.html")

@frontend_bp.route("/leds", methods=["GET", "POST"])
def leds():
    
    return render_template("leds.html")
=======
    return render_template("admin.html")
>>>>>>> upstream/main

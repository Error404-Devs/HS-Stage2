import requests
from flask import render_template
from . import frontend_bp  # Import the frontend_bp blueprint


@frontend_bp.route("/")
def index():
    # Make an API call to the API route we created
    response = requests.get("http://127.0.0.1:5000/api/data")
    print(response)

    # Assuming the response is a JSON object, extract the message
    api_data = (
        response.json()
        if response.status_code == 200
        else {"message": "API call failed"}
    )

    # Pass the message to the template
    return render_template("index.html", message=api_data["message"])


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

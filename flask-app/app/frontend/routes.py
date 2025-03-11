import requests
from flask import render_template
from . import frontend_bp  # Import the frontend_bp blueprint

@frontend_bp.route('/')
def index():
    # Make an API call to the API route we created
    response = requests.get('http://127.0.0.1:5000/data')
    print(response)
    
    # Assuming the response is a JSON object, extract the message
    api_data = response.json() if response.status_code == 200 else {"message": "API call failed"}

    # Pass the message to the template
    return render_template('index.html', message=api_data['message'])

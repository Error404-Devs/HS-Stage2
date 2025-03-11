from flask import Blueprint

frontend_bp = Blueprint('frontend', __name__)

from . import routes  # Import the routes from the current directory

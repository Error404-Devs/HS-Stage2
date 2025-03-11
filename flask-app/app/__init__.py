from flask import Flask
from app.api import api_bp
from app.frontend import frontend_bp

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object('app.config.Config')
    
    # Register blueprints
    app.register_blueprint(frontend_bp)
    app.register_blueprint(api_bp)  # API blueprint has url_prefix='/api'

    return app

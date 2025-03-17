from flask import Flask
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__, 
                static_folder='../static',
                template_folder='../templates')
    
    # Enable CORS
    CORS(app)
    
    # Configure upload folders
    app.config['UPLOAD_FOLDER'] = os.path.join(app.static_folder, 'uploads')
    app.config['RESULTS_FOLDER'] = os.path.join(app.static_folder, 'results')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
    
    # Ensure upload directories exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['RESULTS_FOLDER'], exist_ok=True)
    
    # Register routes
    from app.routes import main
    app.register_blueprint(main)
    
    return app

# Create the Flask application instance
app = create_app() 
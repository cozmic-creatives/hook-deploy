from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    from app.routes.storybook_webhook import webhook_bp
    app.register_blueprint(webhook_bp)
    
    return app 
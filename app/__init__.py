from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    from app.routes.storybook_webhook import storybook_webhook_bp
    app.register_blueprint(storybook_webhook_bp)
    
    return app 
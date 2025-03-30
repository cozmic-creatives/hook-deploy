from flask import Blueprint, request, jsonify

storybook_webhook_bp = Blueprint('storybook_webhook', __name__, url_prefix='/webhook')

@storybook_webhook_bp.route('/storybook', methods=['POST'])
def storybook_hook():
    """
    Endpoint to handle Storybook webhook requests
    """
    data = request.json
    # Process the webhook data here
    
    return jsonify({"status": "success", "message": "Webhook received"}), 200

@storybook_webhook_bp.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint for health checks
    """
    return jsonify({"status": "healthy"}), 200
from flask import Blueprint, request, jsonify
import requests
import os

webhook_bp = Blueprint('webhook', __name__, url_prefix='/webhook')

# Load secret from environment variable
COOLIFY_TOKEN = os.environ.get('COOLIFY_TOKEN')

@webhook_bp.route('/storybook', methods=['POST'])
def storybook_hook():
    # Directly trigger Coolify deployment without verification
    url = 'http://coolify.matthewbracke.com/api/v1/deploy?uuid=bk088owo0wcksg4ooksckos4&force=false'
    headers = {
        'Authorization': f'Bearer {COOLIFY_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        return 'Deploy triggered successfully', 200
    else:
        return f'Failed to trigger deploy: {response.status_code}', 500

@webhook_bp.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint for health checks
    """
    return jsonify({"status": "healthy"}), 200
from flask import Blueprint

another_bp = Blueprint('another', __name__)

@another_bp.route('/another_endpoint', methods=['GET'])
def another_endpoint():
    return 'This is another endpoint', 200
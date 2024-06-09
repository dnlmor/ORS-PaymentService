from flask import Blueprint, request, jsonify

bp = Blueprint('routes', __name__)

@bp.route('/pay', methods=['POST'])
def process_payment():
    data = request.get_json()
    # Here you would integrate with a real payment gateway
    return jsonify({'message': 'Payment processed successfully', 'amount': data['amount']})

import uuid
import random

def generate_transaction_id():
    return str(uuid.uuid4())

def process_payment_with_gateway(amount, payment_method):
    # This is a mock function to simulate payment processing
    # In a real-world scenario, you would integrate with an actual payment gateway
    success = random.choice([True, False])
    message = "Payment successful" if success else "Payment failed"
    return success, message

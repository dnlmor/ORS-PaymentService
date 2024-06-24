from .models import Payment, PaymentStatus
from .database import db_session
from .utils import generate_transaction_id, process_payment_with_gateway
from sqlalchemy.exc import IntegrityError

class PaymentService:
    @staticmethod
    def process_payment(order_id, amount, payment_method):
        try:
            transaction_id = generate_transaction_id()
            
            # Simulate payment processing with a payment gateway
            success, message = process_payment_with_gateway(amount, payment_method)
            
            status = PaymentStatus.COMPLETED if success else PaymentStatus.FAILED
            
            payment = Payment(
                order_id=order_id,
                amount=amount,
                status=status,
                payment_method=payment_method,
                transaction_id=transaction_id
            )
            
            db_session.add(payment)
            db_session.commit()
            return payment
        except IntegrityError:
            db_session.rollback()
            raise ValueError("Failed to process payment")

    @staticmethod
    def get_payment_by_id(id):
        payment = Payment.query.get(id)
        if not payment:
            raise ValueError("Payment not found")
        return payment

    @staticmethod
    def list_payments(order_id=None):
        query = Payment.query
        if order_id:
            query = query.filter_by(order_id=order_id)
        return query.all()

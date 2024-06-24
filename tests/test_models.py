import unittest
from app.models import Payment, PaymentStatus
from app.database import db_session

class TestPaymentModel(unittest.TestCase):
    def setUp(self):
        self.payment = Payment(
            order_id=1,
            amount=100.50,
            status=PaymentStatus.PENDING,
            payment_method="CREDIT_CARD",
            transaction_id="test_transaction_id"
        )

    def test_create_payment(self):
        db_session.add(self.payment)
        db_session.commit()
        self.assertIsNotNone(self.payment.id)

    def tearDown(self):
        db_session.remove()

if __name__ == '__main__':
    unittest.main()

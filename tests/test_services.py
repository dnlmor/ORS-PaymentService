import unittest
from app.services import PaymentService
from app.models import Payment, PaymentStatus
from app.database import db_session

class TestPaymentService(unittest.TestCase):
    def setUp(self):
        self.payment_data = {
            'order_id': 1,
            'amount': 100.50,
            'payment_method': "CREDIT_CARD"
        }

    def test_process_payment(self):
        payment = PaymentService.process_payment(**self.payment_data)
        self.assertIsNotNone(payment.id)
        self.assertEqual(payment.order_id, self.payment_data['order_id'])
        self.assertEqual(payment.amount, self.payment_data['amount'])
        self.assertEqual(payment.payment_method, self.payment_data['payment_method'])
        self.assertIsNotNone(payment.transaction_id)
        self.assertIn(payment.status, [PaymentStatus.COMPLETED, PaymentStatus.FAILED])

    def tearDown(self):
        db_session.remove()

if __name__ == '__main__':
    unittest.main()

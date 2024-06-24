import unittest
from app import create_app
from app.models import db_session, Payment

class TestSchema(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        db_session.remove()

    def test_process_payment(self):
        response = self.client.post('/graphql', json={'query': '''
            mutation {
                processPayment(orderId: 1, amount: 100.50, paymentMethod: "CREDIT_CARD") {
                    payment {
                        id
                        orderId
                        amount
                        status
                        paymentMethod
                        transactionId
                    }
                }
            }
        '''})
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json)

    def test_get_payment(self):
        # First, process a payment
        self.test_process_payment()
        
        response = self.client.post('/graphql', json={'query': '''
            query {
                getPayment(id: 1) {
                    id
                    orderId
                    amount
                    status
                    paymentMethod
                    transactionId
                }
            }
        '''})
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json)

if __name__ == '__main__':
    unittest.main()

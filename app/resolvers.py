from .services import PaymentService

def resolve_process_payment(info, order_id, amount, payment_method):
    return PaymentService.process_payment(order_id, amount, payment_method)

def resolve_get_payment(info, id):
    return PaymentService.get_payment_by_id(id)

def resolve_list_payments(info, order_id=None):
    return PaymentService.list_payments(order_id)

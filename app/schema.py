import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Payment
from app import db

class PaymentType(SQLAlchemyObjectType):
    class Meta:
        model = Payment

class ProcessPayment(graphene.Mutation):
    payment = graphene.Field(PaymentType)

    class Arguments:
        order_id = graphene.Int(required=True)
        amount = graphene.Float(required=True)
        payment_method = graphene.String(required=True)
        address = graphene.String()

    def mutate(self, info, order_id, amount, payment_method, address=None):
        payment = Payment(
            order_id=order_id,
            amount=amount,
            payment_method=payment_method,
            address=address
        )
        db.session.add(payment)
        db.session.commit()
        return ProcessPayment(payment=payment)

class UpdatePaymentStatus(graphene.Mutation):
    payment = graphene.Field(PaymentType)

    class Arguments:
        payment_id = graphene.Int(required=True)
        status = graphene.String(required=True)

    def mutate(self, info, payment_id, status):
        payment = Payment.query.get(payment_id)
        if not payment:
            raise ValueError("Payment not found")

        payment.status = status
        db.session.commit()

        return UpdatePaymentStatus(payment=payment)

class Query(graphene.ObjectType):
    payment = graphene.Field(PaymentType, id=graphene.Int())
    payments = graphene.List(PaymentType, order_id=graphene.Int())

    def resolve_payment(self, info, id):
        return Payment.query.get(id)

    def resolve_payments(self, info, order_id):
        return Payment.query.filter_by(order_id=order_id).all()

class Mutation(graphene.ObjectType):
    process_payment = ProcessPayment.Field()
    update_payment_status = UpdatePaymentStatus.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

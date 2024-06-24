import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from .models import Payment as PaymentModel, PaymentStatus
from .resolvers import (
    resolve_process_payment, resolve_get_payment, resolve_list_payments
)

class PaymentStatusEnum(graphene.Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Payment(SQLAlchemyObjectType):
    class Meta:
        model = PaymentModel

class Query(graphene.ObjectType):
    get_payment = graphene.Field(Payment, id=graphene.Int(required=True))
    list_payments = graphene.List(Payment, order_id=graphene.Int())

    def resolve_get_payment(self, info, id):
        return resolve_get_payment(info, id)

    def resolve_list_payments(self, info, order_id=None):
        return resolve_list_payments(info, order_id)

class ProcessPayment(graphene.Mutation):
    class Arguments:
        order_id = graphene.Int(required=True)
        amount = graphene.Float(required=True)
        payment_method = graphene.String(required=True)

    payment = graphene.Field(lambda: Payment)

    def mutate(self, info, order_id, amount, payment_method):
        return resolve_process_payment(info, order_id, amount, payment_method)

class Mutation(graphene.ObjectType):
    process_payment = ProcessPayment.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

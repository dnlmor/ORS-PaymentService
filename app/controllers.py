from flask import Blueprint
from flask_graphql import GraphQLView
from .schema import schema

payment_blueprint = Blueprint('payment', __name__)

payment_blueprint.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

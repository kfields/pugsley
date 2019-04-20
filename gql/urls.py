from django.urls import path
from . import views
from graphene_django.views import GraphQLView
#TODO:  Isn't there a way to use csrf?  Why was GrapiQl working and not Playground?
from django.views.decorators.csrf import csrf_exempt

class MyGraphQLView(GraphQLView):
    def __init__(self, *args, **kwargs):
        self.graphiql_template = "gql/playground.html"
        super(MyGraphQLView, self).__init__(*args, **kwargs)

urlpatterns = [
    # path('', GraphQLView.as_view(graphiql=True)),
    path('', csrf_exempt(MyGraphQLView.as_view(graphiql=True))),
]
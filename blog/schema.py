from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Post

class PostNode(DjangoObjectType):
    class Meta:
        model = Post
        filter_fields = []
        interfaces = (relay.Node, )

class Query(object):
    post = relay.Node.Field(PostNode)
    all_posts = DjangoFilterConnectionField(PostNode)
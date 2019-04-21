import graphene

import myaccount.schema
import blog.schema


class Query(myaccount.schema.Query, blog.schema.Query, graphene.ObjectType):
    pass

class Mutation(myaccount.schema.Mutation, blog.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
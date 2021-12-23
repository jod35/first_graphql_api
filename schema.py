from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
from models import (
    User as UserModel,
    Post as PostModel
)
from graphene import ObjectType,Schema
from models import engine
from sqlalchemy.orm import sessionmaker

Session=sessionmaker()

session=Session(bind=engine)

class User(SQLAlchemyObjectType):
    class Meta:
        model=UserModel
        interfaces=(relay.Node,)


class Post(SQLAlchemyObjectType):
    class Meta:
        model=PostModel
        interfaces=(relay.Node,)


class Query(ObjectType):
    node=relay.Node.Field()

    all_users=SQLAlchemyConnectionField(User)

    all_posts=SQLAlchemyConnectionField(Post)


    def resolve_all_users(root,info):
        return session.query(UserModel).all()

    def resolve_all_posts(root,info):
        return session.query(PostModel).all()




schema=Schema(query=Query)





from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from schema import schema



app=FastAPI()


@app.get('/')
async def index():
    return {"message":"Hello World"}


app.add_route('/graphql',GraphQLApp(schema=schema))
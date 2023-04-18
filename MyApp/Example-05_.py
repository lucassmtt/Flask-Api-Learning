from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel


myServer = Flask(__name__)
spec = FlaskPydanticSpec('Flask', title='Motta"s API')
spec.register(myServer)


class People(BaseModel):
    id: int
    age: int
    name: str


@myServer.get('/people')
@spec.validate(resp=Response(HTTP_200=People))
def get_people():
    return 'Nobody'


@myServer.post('/people')
@spec.validate(
    body=Request(People), resp=Response(HTTP_200=People)
)
def insert_people():
    """
    Insert one people in DB
    :return: Body
    """
    body = request.context.body.dict()
    return body


myServer.run()
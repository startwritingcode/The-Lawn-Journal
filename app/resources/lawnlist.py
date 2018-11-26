import json
from flask import jsonify, request
from flask_restful import Resource, reqparse
from app.utilities.lawnbuilder import buildLawn
from app.models.lawn import Lawn
from app.models.address import Address

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help="Name field is required")

class LawnListApi(Resource):
    def __init__(self, **kwargs):
        self.mongoClient = kwargs['mongo_client']

    def get(self):
        print('Getting all lawns')
        lawn_documents = self.mongoClient.db.lawns.find()
        lawns = list(map(lambda x: Lawn.deserialize(x), lawn_documents))

        response = jsonify(lawns=[l.serialize() for l in lawns])
        response.status_code = 200
        return response

    def post(self):
        print('Creating a new lawn')
        args = parser.parse_args()
        newLawn = Lawn(args['name'])

        lawnJson = newLawn.serialize()
        newLawnId = self.mongoClient.db.lawns.insert_one(lawnJson).inserted_id
        newLawn.id = newLawnId

        response = jsonify(newLawn.serialize())
        response.status_code = 201
        return response
    
    


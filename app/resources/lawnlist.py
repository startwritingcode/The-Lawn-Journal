import json
from flask import jsonify, request
from flask_restful import Resource
from app.utilities.lawnbuilder import buildLawn

# Only imported for sample data
from app.resources.testdata import LAWNS

class LawnListApi(Resource):
    def get(self):
        print('Getting all lawns')

        response = jsonify(lawns=[l.serialize() for l in LAWNS])
        response.status_code = 200
        return response

    def post(self):
        print('Creating a new lawn')
        lawn_dict = json.loads(request.data)

        lawn = buildLawn(lawn_dict)
        LAWNS.append(lawn)
    
        response = jsonify(lawn.serialize())
        response.status_code = 201
        return response
    
    


import json
from flask import jsonify, request
from flask_restful import Resource
from app.utilities.lawnbuilder import buildLawn
from bson.objectid import ObjectId
from app.models.lawn import Lawn

# Only imported for sample data
from app.resources.testdata import LAWNS

class LawnApi(Resource):
    def __init__(self, **kwargs):
        self.mongoClient = kwargs['mongo_client']

    def get(self, lawn_id):
        print('Getting lawn with id: %s' % lawn_id)
        lawn_document = self.mongoClient.db.lawns.find_one({'_id': ObjectId(lawn_id)})
        if lawn_document is not None:
            lawn = Lawn.deserialize(lawn_document)
            response = jsonify(lawn.serialize())
            response.status_code = 200
            return response
        else:
            message = {
                'status': 404,
                'message': 'Lawn at index %s not found' % index
            }
            response = jsonify(message)
            response.status_code = 404
            return response

    def put(self, lawn_id):
        print('Update lawn with id: %s' % lawn_id)
        lawn = self.getLawn(lawn_id)
        if lawn is not None:
            updated_lawn_dict = json.loads(request.data)
            updated_lawn = buildLawn(updated_lawn_dict)
            lawn.name = updated_lawn.name
            lawn.address = updated_lawn.address
            lawn.total_area = updated_lawn.total_area
            lawn.unit_of_measurement = updated_lawn.unit_of_measurement

            response = jsonify(lawn.serialize())
            response.status_code = 200
            return response
        else:
            message = {
                'status': 404,
                'message': 'Lawn at index %s not found' % index
            }
            response = jsonify(message)
            response.status_code = 404
            return response
    
    def delete(self, lawn_id):
        print('Deleting lawn with id: %s' % lawn_id)

        lawn = self.getLawn(lawn_id)
        if lawn is not None:
            LAWNS.pop(int(lawn_id))
            response = jsonify({})
            response.status_code = 200
            return response

    def getLawn(self, id):
        try:
            int_id = int(id)
            if int_id <= len(LAWNS):
                return LAWNS[int_id]
            else: 
                return None
        except ValueError:
            return None

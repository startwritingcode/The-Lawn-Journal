from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Lawn(Resource):
    def get(self, lawn_id):
        print('Getting lawn with id: %s' % lawn_id)

    def put(self, lawn_id):
        print('Update lawn with id: %s' % lawn_id)
    
    def delete(self, lawn_id):
        print('Deleting lawn with id: %s' % lawn_id)

class LawnList(Resource):
    def get(self):
        print('Getting all lawns')

    def post(self):
        print('Creating a new lawn')

api.add_resource(HelloWorld, '/')
api.add_resource(LawnList, '/lawns')
api.add_resource(Lawn, '/lawns/<lawn_id>')

if __name__ == '__main__':
    app.run(debug=True)
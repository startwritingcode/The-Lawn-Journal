from flask import Flask
from flask_restful import Resource, Api

from resources.lawn import LawnApi
from resources.lawnlist import LawnListApi

app = Flask(__name__)
api = Api(app)

api.add_resource(LawnListApi, '/lawns')
api.add_resource(LawnApi, '/lawns/<lawn_id>')

if __name__ == '__main__':
    app.run(debug=True)
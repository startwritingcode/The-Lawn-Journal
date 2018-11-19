from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_pymongo import PyMongo

from app.resources.lawn import LawnApi
from app.resources.lawnlist import LawnListApi

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/lawnjournal"
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)
mongo = PyMongo(app)

api.add_resource(LawnListApi, '/api/lawns')
api.add_resource(LawnApi, '/api/lawns/<lawn_id>')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask_restful import Resource, Api
import db.rest_commands
from api.brand_api_commands import Brands
# import firebase_admin
# from firebase_admin import credentials, db

# Initialize Firebase Admin SDK with your service account credentials
# cred = credentials.Certificate('/Users/tmg2102/budgetbuddy-61c1b-firebase-adminsdk-in3rm-3036a049b4.json')
# firebase_admin.initialize_app(cred)

app = Flask(__name__)
api = Api(app)

api.add_resource(Brands, '/items', '/<string:brand>')

if __name__ == '__main__':
    # db.rest_commands.setUp() t
    app.run(debug=True, host='10.200.83.180',port=4999)

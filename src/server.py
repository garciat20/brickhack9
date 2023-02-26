from flask import Flask
from flask_restful import Resource, Api
import db.rest_commands
from api.brand_api_commands import Brands

app = Flask(__name__)
api = Api(app)

api.add_resource(Brands, '/items')



if __name__ == '__main__':
    db.rest_commands.setUp()
    app.run(debug=True, port=4999)
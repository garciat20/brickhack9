from flask import Flask
from flask_restful import Resource, Api
import db.rest_commands

app = Flask(__name__)
api = Api(app)




if __name__ == '__main__':
    db.rest_commands.setUp()
    app.run(debug=True, port=4999)
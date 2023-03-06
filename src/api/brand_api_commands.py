import flask_restful
import db.rest_commands

class Brands(flask_restful.Resource):
    def get(self, brand=None):
        if (brand != None):
            return db.rest_commands.get_brand_items(brand)
        return db.rest_commands.get_all_items()

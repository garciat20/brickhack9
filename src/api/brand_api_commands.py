import flask_restful
import db.rest_commands

class Brands(flask_restful.Resource):
    def get(self, name=None, category=None):
        if (name != None and category != None):
            return db.rest_commands.brand_and_category_items(name,category)
        if (name == None and category==None):
           return db.rest_commands.get_all_items()
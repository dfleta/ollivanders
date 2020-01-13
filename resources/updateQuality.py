from flask_restful import Resource, Api
from config import tienda
from services.service import updateQuality


class UpdateQuality(Resource):

    def get(self):
        return updateQuality(tienda)

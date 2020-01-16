from flask_restful import Resource, Api
from config import tienda
from services.service import Service


class UpdateQuality(Resource):

    def get(self):
        return Service.updateQuality(tienda)

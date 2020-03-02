from flask_restful import Resource, Api
from repository.models import Item
from services.service import Service


class Inventario(Resource):

    def get(self):
        return Service.inventario(Item)

    def post(self):
        pass

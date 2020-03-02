from flask_restful import Resource, Api
from repository.models import Item
from services.service import Service


class Items(Resource):

    def get(self, itemName):
        return Service.getItem(Item, itemName)

    def post(self):
        pass

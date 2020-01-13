from flask_restful import Resource, Api
from config import tienda
from services.service import getInventario


class Inventario(Resource):

    def get(self):
        return getInventario(tienda)

    def post(self):
        pass

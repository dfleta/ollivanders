from flask_restful import Resource, Api, reqparse
from repository.models import Item
from services.service import Service


class Items(Resource):

    def get(self, itemName):
        return Service.getItem(Item, itemName)

    def post(self):
        # curl -d name="Conjured Mana Cake" -d sell_in=3 -d quality=6 http://127.0.0.1:5000/items
        # validar el objeto flask.Request.values
        # o flask.Request.json
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('name', type=str, required=True,
                            help='name required')
        parser.add_argument('sell_in', type=int, required=True,
                            help='sellIn required')
        parser.add_argument('quality', type=int, required=True,
                            help='quality required')
        # args es un diccionario con los argumentos
        # especificados como keys
        args = parser.parse_args()
        Service.postItem(Item, args)

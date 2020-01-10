from flask import Flask
from flask_restful import Resource, Api

from service import getInventario
from repo import initRepo

tienda = initRepo()

app = Flask(__name__)
api = Api(app)


class Ollivanders(Resource):

    def get(self):
        return {'Welcome!': 'Ollivanders'}


class Inventario(Resource):

    def get(self):
        # return {'Inventario': 'Ollivanders'}
        return getInventario(tienda)


class UpdateQuality(Resource):

    def get(self):
        return {'updated': 'Items'}


api.add_resource(Ollivanders, '/')
api.add_resource(Inventario, '/inventario')
api.add_resource(UpdateQuality, '/updateQuality')


if __name__ == '__main__':
    app.run(debug=True)

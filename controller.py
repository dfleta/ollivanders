from flask import Flask
from flask_restful import Resource, Api

from repository.repo import initRepo
from resources.inventario import Inventario
from resources.updateQuality import UpdateQuality
from config import *

app = Flask(__name__)
api = Api(app)


class Ollivanders(Resource):

    def get(self):
        return {'Welcome!': 'Ollivanders'}


api.add_resource(Ollivanders, '/')
api.add_resource(Inventario, '/inventario')
api.add_resource(UpdateQuality, '/updateQuality')


if __name__ == '__main__':
    app.run(debug=True)

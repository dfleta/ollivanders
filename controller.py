from flask import Flask
from flask_restful import Resource, Api

from resources.inventario import Inventario
from resources.updateQuality import UpdateQuality
from resources.root import Root
from resources.items import Items
from resources.quality import Quality
from resources.sellin import SellIn


# from config import *

# from repository.db import initialize_db
# from flask_mongoengine import MongoEngine
# from repository.models import Item
from repository.db import *

app = Flask(__name__)

# API REST
api = Api(app)
api.add_resource(Root, '/')
api.add_resource(Inventario, '/inventario')
api.add_resource(UpdateQuality, '/update-quality')
api.add_resource(Items, '/items/name/<itemName>', '/items')
api.add_resource(Quality, '/items/quality/<itemQuality>')
api.add_resource(SellIn, '/items/sellin/<itemSellIn>')


if __name__ == '__main__':
    app.run(debug=True)

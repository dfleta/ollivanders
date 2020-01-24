from pymongo import MongoClient
from mongoengine import *
from repository.models import Item

# conectar con MongoDB
client = MongoClient()
# client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017/')

# obteniendo una bbdd
client.drop_database('ollivanders')
db = client['ollivanders']
# db = client.ollivanders

# Getting a Collection¶
collection = db['inventario']

# mongoengine: how to connect to our instance of mongod:
connect('ollivanders')

# adding data
item = Item(name="+5 Dexterity Vest")
item.sell_in = 10
item.quality = 20
item.save()

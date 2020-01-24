from mongoengine import *


class Item(Document):

    name = StringField(required=True)
    sell_in = IntField()
    quality = IntField()

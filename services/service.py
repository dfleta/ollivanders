
from flask import Response
from flask_restful import fields, marshal_with


class Service():

    resource_fields = {
            'name': fields.String,
            'sell_in': fields.Integer,
            'quality': fields.Integer
    }

    @marshal_with(resource_fields)
    def getInventario(Item):
        listItems = []
        for item in Item.objects():
            listItems.append(item)
        return listItems

    def updateQuality(tienda):
        tienda.update_quality()
        return Service.getInventario(tienda)

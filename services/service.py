
from flask import Response
from flask_restful import fields, marshal_with
from domain.test_gilded_rose import crearObjetoItem


class Service():

    resource_fields = {
            'name': fields.String,
            'sell_in': fields.Integer,
            'quality': fields.Integer
    }

    @staticmethod
    @marshal_with(resource_fields)
    def getInventario(Item):
        listItems = []
        for item in Item.objects():
            listItems.append(item)
        return listItems

    @staticmethod
    def updateQuality(Item):
        for item in Item.objects():
            itemObject = crearObjetoItem(
                [item.name, item.sell_in, item.quality])
            itemObject.update_quality()
            item.sell_in = itemObject.sell_in
            item.quality = itemObject.quality
            item.save()

        # ayudaria un id en el objeto para
        # encontrarlo en la base de datos

        return Service.getInventario(Item)

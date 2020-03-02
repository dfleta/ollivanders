
from flask import Response
from flask_restful import fields, marshal_with
from repository.models import Item

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

    @staticmethod
    @marshal_with(resource_fields)
    def getItem(Item, itemName):
        # objects(name="Aged Brie") = QuerySet that will
        # only iterate over items =>
        # devuelve una coleccion => recogerla en lista
        # antes de devolver
        listItems = []
        for item in Item.objects(name=itemName):
            listItems.append(item)
            # hay que resolver el tema del espacio
            # en blanco en la url en aged brie
            # de momento usar %20 como espacio
        return listItems

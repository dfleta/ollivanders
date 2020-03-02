
from flask import Response
from flask_restful import fields, marshal_with, abort
from repository.models import Item
from mongoengine.queryset.visitor import Q

from domain.test_gilded_rose import crearObjetoItem


class Service():

    resource_fields = {
            'name': fields.String,
            'sell_in': fields.Integer,
            'quality': fields.Integer
    }

    @staticmethod
    @marshal_with(resource_fields)
    def inventario(Item):
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

        return Service.inventario(Item)

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
            # Hay que resolver el tema del espacio
            # en blanco en la url en aged brie
            # De momento usar %20 como espacio
        if not listItems:
            abort(404, message="El item {} no existe".format(itemName))
        return listItems

    @staticmethod
    def postItem(Item, args):
        item = Item(name=args['name'])
        item.sell_in = args['sell_in']
        item.quality = args['quality']
        item.save()

    @staticmethod
    @marshal_with(resource_fields)
    def filterQuality(Item, itemQuality):
        listItems = []
        for item in Item.objects(Q(quality=itemQuality)):
            listItems.append(item)
        if not listItems:
            abort(404, message="No existen items que satisfagan criterios")
        return listItems

    @staticmethod
    def deleteItem(Item, args):
        item = Item.objects(Q(name=args['name'])
                            & Q(sell_in=args['sell_in'])
                            & Q(quality=args['quality']))
        if not item:
            abort(404, message="No existe el item")
        else:
            item.delete()

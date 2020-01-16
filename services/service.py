
class Service():

    def getInventario(tienda):
        inventario = {}
        items = tienda.getItems()

        for item in items:
            inventario[item.name] = item.__dict__
        return inventario

    def updateQuality(tienda):
        tienda.update_quality()
        return Service.getInventario(tienda)

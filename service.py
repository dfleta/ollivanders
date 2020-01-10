

def getInventario(tienda):
    # return {'Inventario': 'Ollivanders'}
    inventario = {}
    items = tienda.getItems()

    for item in items:
        inventario[item.name] = {'sell_in': item.sell_in, 'quality': item.quality}

    return inventario

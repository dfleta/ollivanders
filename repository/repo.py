from domain.types import *
from domain.accesoCasosTexttest_deudatecnica_saneada import *


class SingletonOllivander():

    instanciaTienda = None

    def crearTienda():
        if not SingletonOllivander.instanciaTienda:
            SingletonOllivander.instanciaTienda = SingletonOllivander.initRepo()
        return SingletonOllivander.instanciaTienda

    def initRepo():

        rutaAccesoFichero = "domain/stdout_bug_conjured.gr"

        matrizCasosTest = []

        matrizCasosTest = accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero)

        items = SingletonOllivander.extraerItemsIventario(matrizCasosTest)

        inventario = []
        for item in items:
            objetoItem = SingletonOllivander.crearObjetoItem(item)
            assert isinstance(objetoItem.sell_in, int)
            assert isinstance(objetoItem.quality, int)
            inventario.append(objetoItem)

        tienda = GildedRose(inventario)
        return tienda

    def extraerItemsIventario(matrizCasosTest):
        """
        Extrae los items y el estado en el que están el primer dia
        de los casos test y devuelve una lista de items:
        items = [ [item], [item], [item] ]

        Argumentos:
        matrizCasostest -> lista con los casos test. Cada elemento es un dia
        """
        return matrizCasosTest[0]

    def crearObjetoItem(item):
        """
        Devuelve un objeto de la clase Item.

        Es necesario convertir la segunda y tercera propiedad a int.

        Argumentos:
        item = ['Elixir of the Mongoose', ' 5', ' 7']
        """
        diccionarioClases = {"Sulfuras, Hand of Ragnaros": "Sulfuras",
                            "Aged Brie": "AgedBrie",
                            "Backstage passes to a TAFKAL80ETC concert": "Backstage",
                            "Conjured Mana Cake": "ConjuredItem",
                            "+5 Dexterity Vest": "ConjuredItem",
                            "Normal Item": "NormalItem"}

        try:
            nombreItem = item[0]
            clase = diccionarioClases[nombreItem]
        except KeyError:
            clase = diccionarioClases["Normal Item"]
        finally:
            return eval(clase + str(tuple(item)))

    def test(tienda, estadoInventario):

        nombrePropiedadesItem = ["name", "sell_in", "quality"]
        numeroPropiedadesItem = len(nombrePropiedadesItem)

        for (offset, item) in enumerate(tienda.items):
            print(item)
            for i in range(1, numeroPropiedadesItem):
                propiedad = nombrePropiedadesItem[i]
                valorPropiedadCasoTest = estadoInventario[offset][i]
                assert getattr(item, propiedad) == valorPropiedadCasoTest, \
                    "falla %s %s %s" % (propiedad, estadoInventario[offset][i], item.__class__.__name__)

##############################################################
from random import randint
from platos import Comestible, Bebestible
## Si necesita agregar imports, debe agregarlos aquí arriba ##
import random #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

### INICIO PARTE 2.1 ###
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self)
        super().__init__(nombre)
        self.tiempo_entrega = random.randint(20, 30)
        self.energia = random.randint(75, 100)
    
    def repartir(pedido):
        pass

### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero:
    pass 
### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente:
    pass
### FIN PARTE 2.4 ###

if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Jugo Natural": ["Jugo Natural", "Bebestible"],
        "Empanadas": ["Empanadas", "Comestible"],
        }
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        un_repartidor = Repartidor("Tomás", randint(20, 30))
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA)
        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")

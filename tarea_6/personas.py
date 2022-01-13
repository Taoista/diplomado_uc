##############################################################
from random import randint
from platos import Comestible, Bebestible
import random 
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 2.1 ###
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self,nombre, tiempo_entrega):
        super().__init__(nombre)
        self.tiempo_entrega = tiempo_entrega #random 20,30
        self.energia = random.randint(75, 100)
    
    def repartir(pedido):
        factor_tamano = 0

        if len(pedido) <=2:
            factor_tamano = 5
            self.energia = self.energia - factor_tamano
        else:
            factor_tamano = 15
            self.energia = self.energia - factor_tamano

        fac_vel = 0
        if len(pedido) <=2:
            fac_vel = 1.25
            self.tiempo_entrega = self.tiempo_entrega * fac_vel
        else:
            tiempo_entrega = 0.85
            self.tiempo_entrega = self.tiempo_entrega * fac_vel

        print(f"El repartidor {self.nombre} se ha demorado {self.tiempo_entrega} y perdiendo {self.energia} ")


### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, nombre,habilidad):
        super().__init__(nombre)
        self.habilidad = habilidad
        self.energia = random.randint(50,80)

    def cocinar(informacion_plato):
        for i in informacion_plato.values():
            if i[1] == "Bebestible":
                new_bbstible = Bebestible(i[0])
                if new_bbstible.dificultad == 3:
                    new_bbstible.energia = new_bbstible.energia -5

                if new_bbstible.dificultad == 6:
                    new_bbstible.energia = new_bbstible.energia -8
                
                if new_bbstible.dificultad == 6:
                    new_bbstible.energia = new_bbstible.energia -10

                if new_bbstible.dificultad > self.habilidad:
                    new_bbstible.calidad = new_bbstible.calidad * 0.7
                else:
                    new_bbstible.calidad = new_bbstible.calidad * 1.5


            if i[1] == "Comestible":
                new_comest = Comestible(i[0])
                new_comest.energia = new_comest.energia - 15
            
        print(f"El cocinero {self.nombre} ha cocinado {new_bbstible.nombre} perdiendo {self.energia} de energía")
        print(new_bbstible)
        print(new_comest)
        
        return  new_bbstible is None: new_bbstible :  new_comest



### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self, nombre, platos_preferidos):
        super().__init__(nombre)
        self.platos_preferidos = platos_preferidos

    def recibir_pedido(pedido, demora):
        calificacion = 10

        if (len(platos_preferidos) > len(pedido)) OR demora > 20:
            calificacion = calificacion / 2
        
        for i in pedido:
            if i.calidad => 11:
                calificacion = calificacion + 1.5
            elif i.calidad <= 8: 
                calificacion = calificacion - 3
            else:
                pass
        
        print(f"El cliente {self.nombre} ha recibido su pedido y le puso la calificación {calificacion}")

    



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

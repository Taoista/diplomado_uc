import parametros as p
import random

###### INICIO PUNTO 1 ######
### Rellenar Clase Automóvil ###
class Automovil:
    def __init__(self, kilometraje, ano):
        self.__kilometraje = kilometraje
        self.ano = ano
        self.ruedas = []
        self.aceleracion = 0
        self.velocidad = 0
        
    def avanzar(self, tiempo):
        self.__kilometraje += self.velocidad * tiempo/3600
  
    def acelerar(self,tiempo):
        self.aceleracion = tiempo * 0.5
        self.velocidad += self.aceleracion * tiempo * 3.6
        self.avanzar(tiempo)
        self.aceleracion = 0


    def frenar(self, tiempo):
        self.aceleracion = self.aceleracion - (tiempo * 0.5)
        
        self.velocidad += self.aceleracion * tiempo * 3.6
        if self.velocidad <= 0:
            self.velocidad = 0
        self.avanzar(tiempo)
        self.aceleracion = 0
    
    def obtener_kilometraje(self):
        return self.__kilometraje
    
    def reemplazar_rueda(self):
        # for rueda in self.ruedas:
        self.ruedas.remove(min(self.ruedas))
        nueva_rueda = Rueda()
        self.ruedas.append(nueva_rueda)

    def __str__(self):
        return f"Fecha vehiculo => {self.ano}, Velocidad => {self.velocidad}, Kilometraje => {self.obtener_kilometraje()}"

###### FIN PUNTO 1 ######


###### INICIO PUNTO 2 ######
### Rellenar Clase Moto ###
class Moto(Automovil): 
    def __init__(self, kilometraje, ano, cilindrada):
        super().__init__(kilometraje, ano)
        self.cilindrada = cilindrada
        for i in range(2):
            self.ruedas.append(Rueda())

    def acelerar(self, tiempo):
        self.acelerar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar("acelerar")

    def frenar(self,tiempo):
        self.frenar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar("frenar")

    def __str__(self):
        return f"Moto del año {self.ano}."
###### FIN PUNTO 2 ######


###### INICIO PUNTO 3 ######
### Rellenar Clase Camión ###
class Camion(Automovil):
    def __init__(self, kilometraje, ano, carga):
        super().__init__(kilometraje, ano)
        self.carga = carga

        for i in range(6):
            nueva_rueda = Rueda()
            self.ruedas.append(nueva_rueda)

        def acelerar(tiempo):
            self.acelerar(tiempo)
        
        for i in self.ruedas:
            i.gastar("acelerar")

        def frenar(tiempo):
            self.frenar(tiempo)
            for i in self.ruedas:
                i.gastar("frenar")

    def __str__(self):
        return f"Camión del año {self.ano}."
###### FIN PUNTO 3 ######


### Esta clase está completa, NO MODIFICAR ###
class Rueda:
    def __init__(self):
        self.resistencia_actual = random.randint(*p.RESISTENCIA)
        self.resistencia_total = self.resistencia_actual
        self.estado = "Perfecto"

    def gastar(self, accion):
        if accion == "acelerar":
            self.resistencia_actual -= 5
        elif accion == "frenar":
            self.resistencia_actual -= 10
        self.actualizar_estado()

    def actualizar_estado(self):
        if self.resistencia_actual < 0:
            self.estado = "Rota"
        elif self.resistencia_actual < self.resistencia_total / 2:
            self.estado = "Gastada"
        elif self.resistencia_actual < self.resistencia_total:
            self.estado = "Usada"

### Esta funcion está completa, NO MODIFICAR ###
def seleccionar():
    for indice in range(len(vehiculos)):
        print(f"[{indice}] {str(vehiculos[indice])}")

    elegido = int(input())
    if elegido >= 0 and elegido < len(vehiculos):
        vehiculo = vehiculos[elegido]
        print("Se seleccionó el vehículo", str(vehiculo))
        return vehiculo
    else:
        print("intentelo denuevo.")


###### INICIO PUNTO 4.2 ######
### Se debe completar cada opción según lo indicado en el enunciado ###
def accion(vehiculo, opcion):
    if opcion == 2: #Acelerar
        tiempo = int(input("Seleccione el timepo prara acelerar"))
        vehiculo.acelerar(tiempo)
    elif opcion == 3: #Frenar
        tiempo = int(input("Seleccione el timepo prara Frenar"))
        vehiculo.frenar(tiempo)
    elif opcion == 4: #Avanzar
        tiempo = int(input("Seleccione el timepo prara Avanzar"))
        vehiculo.avanzar(tiempo)
    elif opcion == 5: #Cambiar Rueda
        vehiculo.reemplazar_rueda()
    elif opcion == 6: #Mostrar Estado
        print(vehiculo)
###### FIN PUNTO 4.2 ######


if __name__ == "__main__":
    ###### INICIO PUNTO 4.1 ######
    ### Aca deben instanciar los vehiculos indicados
    ### en el enunciado y agregarlos a la lista vehiculos


    motito = Moto(123,1080, 4)
    camioncito = Camion(1234, 1980, 1500)

    vehiculos = []

    vehiculos.append(motito)
    vehiculos.append(camioncito)

    ###### FIN PUNTO 4.1 ######


    ### El codigo de abajo NO SE MODIFICA ###
    vehiculo = vehiculos[0] # Por default comienza seleccionado el primer vehículo  

    dict_opciones = {1: ("Seleccionar Vehiculo", seleccionar),
                     2: ("Acelerar", accion),
                     3: ("Frenar", accion),
                     4: ("Avanzar", accion),
                     5: ("Reemplazar Rueda", accion),
                     6: ("Mostrar Estado", accion),
                     0: ("Salir", None)
                    }

    op = -1
    while op != 0:
        
        for k, v in dict_opciones.items():
            print(f"{k}: {v[0]}")
        
        try:
            op = int(input("Opción: "))
        
        except ValueError:
            print(f"Ingrese opción válida.")
            op = -1
        
        if op != 0 and op in dict_opciones.keys():
            if op == 1:
                vehiculo = dict_opciones[op][1]()
            else:
                dict_opciones[op][1](vehiculo, op)
        elif op == 0:
            pass
        else:
            print(f"Ingrese opción válida.")
            op = -1

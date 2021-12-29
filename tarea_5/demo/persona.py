


class Persona:
    def __init__(self, n, a, id, edad):
        self.nombre = n
        self.apellido = a
        self.rut = id
        self.edad = edad


    def __str__(self):
        return f" Soyu {self.nombre} {self.apellido} y tengo {self.edad}"


    def cumple_anos(self):
        self.edad +=1

    def deme_su_rut(self):
        return self.rut


if __name__ == "__main__":
    c = Persona("Cristian", "olave", "1771823-k", 34)
    d = Persona("Carla", "olave", "123781876-k", 36)



    print(c)
    print(d)

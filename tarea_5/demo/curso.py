class Curso:
    def __init__(self, n,a,s,c,m):
        self.nombre = n
        self.ano = a
        self.semestre = s
        self.credito = c
        self.minimo = m
        self.profesor = None
        self.lista_de_curso = []

    def __str__(self):
        return f"Curso: {self.nombre}"

    def asignar_profesor(self, p):
        self.profesor = p

    def inscribir_alumno(self, alumno):
        self.lista_de_curso.append(alumno)

    def calcular_promedio(self):
        suma = 0
        for est in self.lista_de_curso:
            suma += est.calcular_promedio()

        return suma / len(self.lista_de_curso)

class Profesor:
    def __init__(self,n,e,o,d):
        self.nombre = n
        self.edad = e
        self.oficina = o
        self.departamento = d

    def dictar_clase(self):
        print(f"El profesor {self.nombre} estra dictando la clase.")

    def evaluar_alumno(self, estudiante, nota):
        estudiante.notas.append(nota)


    def __str__(self):
        return f"{self.nombre} del departamento {self.departamento}, oficina: {self.oficina}"


class Estudiantes:
    def __init__(self,m,e,num_al, a):
        self.nombre = m
        self.edad = e
        self.nombre_alumno = num_al
        self.ano = a
        self.avance = 0
        self.notas = []

    def aprueba(self):
        return (sum(self.notas) / len(self.notas)) >= 3.05
    
    def estudiar(self, mins):
        self.avance += 0.05 * mins
    
    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        return f"Estudiante {self.nombre}. Promedio: {self.calcular_promedio()}, Aprueba? {self.aprueba()}"



if __name__ == "__main__":
    curso_dps = Curso("Desarrollo de software", 2021, 1, 10, True)
    profe = Profesor("ToaIdEV", 32, "EO", "123")

    curso_dps.asignar_profesor(profe)
    curso_dps.profesor.dictar_clase()
    print(curso_dps)

    al1 = Alumno("Alumno 1", 30, "121", 2010)
    al2 = Alumno("Alumno 2", 30, "122", 2010)
    al3 = Alumno("Alumno 3", 30, "123", 2010)
    al4 = Alumno("Alumno 4", 30, "124", 2010)
    al5 = Alumno("Alumno 5", 30, "125", 2010)
class alumno:
    def __init__(self, nombre, nota):
        self.nota = nota
        self.nombre = nombre

    def imprimir(self):
        print(self.nombre, "tiene un:", self.nota)

    
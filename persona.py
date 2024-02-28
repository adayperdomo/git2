class persona:
    def __init__(self, nombre, anos):
        self.nombre = nombre
        self.anos = anos

    def imprimir(self):
        print(self.nombre, "tiene:", self.anos)

    def cumpleaños(self):
        print(self.nombre, "cumple:", self.anos)
    
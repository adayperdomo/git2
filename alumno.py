class alumno:

    def nota(promociona):
        promociona = 0
        if promociona >= 5:
            print(alumno, "promociona")
        else:
            print(alumno, "no promociona")

def main():
    paco = alumno()
    paco.nota = 4.99
    paco.promociona()

    pepe = alumno()
    pepe.nota = 5
    pepe.promociona()
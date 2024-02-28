class animal:
    
    def caminar(self):
        self.patas = 0 
        print("caminando con", self.patas, "patas")

def main():
    vaca = animal()
    vaca.patas = 4
    vaca.caminar()
    
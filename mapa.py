class Mapa:
    ##Recibe el tamaño del mapa
    def __init__(self, n:int):
        self.casillas=[[] for _ in range(n)]
        self.n=n
    def insertar(self, elemento):
        posicion= hash(elemento)%self.n
        self.casillas[posicion].append(elemento)
    def buscar(self, elemento):
        posicion= hash(elemento)%self.n
        casilla= self.casillas[posicion]
        if elemento in casilla:
            return True
        else:
            return False
    def __getitem__(self, elemento):
        return self.buscar(elemento)
    def __contains__(self, elemento):
        return self.buscar(elemento)


m= Mapa(10)
print(m.casillas)
m.insertar("Armando")
print(m.casillas)
m.insertar(1.1)
m.insertar(524)
m.insertar("Daniel")
print(m.casillas)
print(m.buscar("Armando"))
print(m.buscar("Pedro"))

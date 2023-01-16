#Gabriel Guerra Rosales y Luis Felipe Organista Méndez
class Arreglo:
    def __init__(self, inicial):
        self.capacidad=inicial
        self.arreglo= [0]*self.capacidad
        self.cantidad=0
    def __repr__(self):
        return str(self.arreglo[:self.cantidad])
    
    def agregar(self,elemento):
        if self.cantidad< self.capacidad:
            self.arreglo[self.cantidad]= elemento
            self.cantidad+=1
            
        else:
            print("El arreglo ya se llenó, no se pudo agregar ", elemento)

    def eliminar(self): ##Eliminar último
        if self.cantidad>0:
            self.cantidad-=1



class ArregloDinamico(Arreglo):
    def agregar(self,elemento): 
        if self.cantidad>=self.capacidad:
            self.capacidad=self.capacidad*2
            temporal=self.arreglo[:self.cantidad]
            self.arreglo = [0]*self.capacidad
            for i in range(self.cantidad):
                self.arreglo[i] = temporal[i]
        super().agregar(elemento)

                
    def eliminar(self):
        super().eliminar()
        self.arreglo[self.cantidad] = 0
        if self.cantidad<int((self.capacidad)*(3/4)):
            self.capacidad=int(self.capacidad*(3/4))
            temporal=self.arreglo[:self.cantidad]
            self.arreglo=[0]*self.capacidad
            for i in range(self.cantidad):
                self.arreglo[i] = temporal[i]
              


b=ArregloDinamico(8)
b.agregar(1)
b.agregar(2)
b.agregar(3)
b.agregar(4)
b.agregar(5)
b.agregar(6)
b.agregar(7)

print(b)
print(b.arreglo)
b.eliminar()
print(b.arreglo)
b.eliminar()
print(b.arreglo)
print(b)
b.agregar(6)
print(b.arreglo)
b.agregar(7)
print(b)
print(b.arreglo)

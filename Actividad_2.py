
from collections import deque


##PROBLEMA ANAGRAMA  

entrada = "madam"
salida = "adamm"

palabra1 = deque(entrada)
palabra2 = deque(salida)

cola = deque()
pila = deque()


pila.append(palabra1.popleft())
print("e", end=" ")

while len(entrada) > len(cola):
    if pila:
        if pila[-1] == palabra2[0]:
            cola.append(pila.pop())
            palabra2.popleft()
            print("s", end=" ")
        else:
            pila.append(palabra1.popleft())
            print("e", end=" ")
    else:
        pila.append(palabra1.popleft())
        print("e", end=" ")
def anagrama(entrada, salida):
    return list(product(entrada, salida))
    
print(anagrama(entrada, salida))


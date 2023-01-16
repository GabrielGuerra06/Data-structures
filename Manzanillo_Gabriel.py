from collections import deque

Caso = 1
palabra = ""

while palabra != "fin":
    palabra = input()
    lista = []

    if palabra != "fin":
        palabra = palabra.upper()

    if palabra == "fin":
        break

    for i in range(len(palabra)):
        A = False
        if len(lista) != 0:
            for j in range(len(lista)):
                Lista = lista[j] 
                if ord(palabra[i]) <= ord(Lista[-1]):
                    A = True
                    lista[j].append(palabra[i])
                    break
        if A == False:
            B = deque()
            lista.append(B)
            lista[-1].append(palabra[i])

    print("Caso " + str(Caso) + ": " + str(len(lista)))
    Caso+= 1
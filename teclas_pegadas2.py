from collections import deque

palabra = input()
final = deque()

encontrar = []

def corchetes(palabra):
    letras = "[]"
    resultado = ""
    for x,i in enumerate(palabra):
        if i not in letras:
            resultado = resultado + str(x) + ","
        else:
            resultado = resultado + " "
    return resultado

def encontrar(palabra):
    encontrar = []
    for x,i in enumerate(palabra):
        if i == "[":
            encontrar.append("start")
        elif i == "]":
            encontrar.append("end")
    return encontrar



def palabras(corchetes):
    arreglo = []
    for i in corchetes:
        letters = ""
        for x in i:
            letters += palabra[int(x)]
        arreglo.append(letters)
    return arreglo


division = corchetes(palabra)
posiciones = []
for i in division.split(" "):
    posiciones.append(i.split(",")[:-1])
letras = palabras(posiciones)
final.append(letras[0])

for index,i in enumerate(encontrar(palabra)):
    if i == "start":
        final.appendleft(letras[index+1])
    elif i == "end":
        final.append(letras[index+1])
print("".join(list(final)))
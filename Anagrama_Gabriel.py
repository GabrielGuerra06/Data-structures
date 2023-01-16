import itertools
from collections import deque

def validar(combinacion, palabra, target):
    dequeP = deque(palabra)
    stack = deque()
    queue = ""
    try:
        for i in combinacion.split(" "):
            if i == "e":
                stack.append(dequeP.popleft())
            else:
                queue += stack.pop()
        if queue == target:
            return True
        else:
            return False
    except:
        return False

palabra2 = input()
cambio = input()
inicio = 'e'
for i in range((len(palabra2)*2)-1):
    inicio = list(itertools.product(inicio,'es'))
    for i in range(len(inicio)):
        inicio[i] = ' '.join(inicio[i])

for i in inicio:
    if validar(i, palabra2, cambio):
        print(i)
pila = list()  

entrada = str(input())  

flag = list()
error = False
e = -1
contador = 0


for char in entrada:
    if char in "({<[":
        flag.append(contador)
        pila.append(char)
    elif char in ")}>]":
        if len(pila) == 0:
            flag.append(contador)
            error = True
            break
##Compara ()
        terminacion = pila.pop()
        if char == ')':
            if terminacion == '(':
                flag.pop()
            else:
                e = contador
                error = True
                break
##Compara {}
        elif char == '}':
            if terminacion == '{':
                flag.pop()
            else:
                error = True
                e = contador
                break
##Compara []
        elif char == ']':
            if terminacion == '[':
                flag.pop()
            else:
                error = True
                e = contador
                break
#Compara < >
        elif char == '>':
            if terminacion == '<':
                flag.pop()
            else:
                error = True
                e = contador
                break
    contador += 1


## IMPRIME ERROR O BALANCEADA
if error or len(flag) > 0:
    while len(pila) > 1:
        flag.pop()

    contador = flag.pop() if e == -1 else e
    print("Error en " , contador)

else:
    print("Balanceada")

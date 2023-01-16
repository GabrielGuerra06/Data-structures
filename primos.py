def criba(limite):
    primos=[]
    pares=[]

    for i in range(2, limite):
        if i not in pares:
            primos.append(i)
        
        for n in range(i*i, limite+1, i):
            pares.append(n)
    if limite in pares:
        return "NO"
    else:
        return"SI"

print(criba(int(input())))

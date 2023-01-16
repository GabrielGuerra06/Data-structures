from math import ceil
n=100
criba=[0]*n

criba[0]= 1
criba[1]= 1

for i in range(2, ceil(n**.5)):
    if not criba[i]:
        for j in range(i+i,n,i):
            criba[j]=1

for j in range(0,n,10):
    print(*criba[i:i+10], sep=" ")


#% https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true

from collections import defaultdict

mapeo = list(map(int,input().split(" ")))
n = mapeo[0]
m = mapeo[1]
diccionario = defaultdict(list)

# Groups A and B inputs
for a in range(n):
    diccionario["A"].append(input())

for b in range(m):
    diccionario["B"].append(input())

# How many times does B appears in A
for x in range(len(diccionario["B"])):
    lista = []
    for y in range(len(diccionario["A"])):
        if diccionario["B"][x] == diccionario["A"][y]:
            lista.append(f"{y+1}")
    if lista != []:
        print(" ".join(lista))
    else:
        print(-1)
    



#% https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true

from itertools import combinations_with_replacement

texto, n = input().split()
texto = list(texto)
texto.sort()
texto = "".join(texto)


lista = list(combinations_with_replacement(texto,int(n)))

lista.sort()

for x in range(len(lista)):
    string=""
    for i in range(len(lista[0])):
        string+=lista[x][i]
    print(string)

from itertools import permutations

texto = input().split(" ")
largo = int(texto[1])

lista = list(permutations(texto[0],largo))

lista.sort() 

for i in range(len(lista)):
    imprimir_texto = ""
    for j in range(largo):
        imprimir_texto += lista[i][j]
    print(imprimir_texto)
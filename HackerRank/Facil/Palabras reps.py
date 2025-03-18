from collections import Counter

n = int(input())

lista_palabras = []

lista_palabras=[input() for x in range(n)]

conteo_palabras = Counter(lista_palabras)

palabras_unicas = list(conteo_palabras.keys())

print(len(palabras_unicas))
print(" ".join(map(str, conteo_palabras.values())))

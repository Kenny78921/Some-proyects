
#% https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

lista_externa = []

for x in range(int(input())):

    name = input()
    score = float(input())
    lista_externa.append([name, score])

minimo = min(lista_externa, key=lambda x: x[1])

penultimo = sorted([estudiante for estudiante in lista_externa if estudiante[1] > minimo[1]], key= lambda x: x[1])
print(penultimo)

segundo = sorted([estudiante[0] for estudiante in penultimo if estudiante[1] == penultimo[0][1]])

for estudiante in segundo:
    print(estudiante)

#% https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

n = int(input())
arr = map(int, input().split(" "))

lista = list(arr)

lista.sort()

for x in range(len(lista)):
    if lista[x] == lista[n-1]:
        segundo = lista[x-1]
        break
        
print(segundo)

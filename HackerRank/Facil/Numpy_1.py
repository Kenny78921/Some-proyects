
#% https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true

import numpy

lista = []
N, M = map(int, input().split())

for x in range(N):
    lista.append(list(map(int, input().split())))

my_array = numpy.array(lista)
max_1 = numpy.min(my_array, axis = 1)
print(numpy.max(max_1))



#% https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
#° Opcion 1
n = int(input())
tupla = tuple(input().split())

var_hash = hash(tupla)
print(tupla)
print(var_hash)

#° Opcion 2 - CORRECTA
n = int(input())
texto = map(int, input().split())
tupla_2 = tuple(texto)

var_hash_2 = hash(tupla_2)

print(tupla_2)
print(var_hash_2)
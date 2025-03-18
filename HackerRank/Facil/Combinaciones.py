
#% https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true

from itertools import combinations

n = int(input())
lista = input().split()
k = int(input())

count = 0
comb = list(combinations(lista,k))
for x in comb:
    if "a" in x:
        count +=1
print(count/len(comb))

#% https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true

N, X = map(int, input().split())
lista = []
nums = list(range(1, 101))

for x in range(X):
    lista.append(list(map(float, input().split())))

zipped = zip(nums,*lista)
for x in list(zipped):
    x = x[1:]
    print(round(sum(x)/X,2))
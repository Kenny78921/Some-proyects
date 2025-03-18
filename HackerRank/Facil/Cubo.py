
#% https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true

def verificar(blocks,n):
    # Funcion si es par
    if n%2 == 0:
        for x in range(int(n/2)-1):
            if blocks[0]>= blocks[1] and blocks[-2] <= blocks[-1]:
                blocks.pop(0)
                blocks.pop(-1)
                print(blocks)
            else:
                return "No"
            
    if n%2 == 1:
        for x in range(int(n/2)):
            if blocks[0]>= blocks[1] and blocks[-2] <= blocks[-1]:
                blocks.pop(0)
                blocks.pop(-1)
                print(blocks)
            else:
                return "No"
    return "Yes"
        
#test = int(input())
test = 1
for x in range(test):
    #% Entrada de datos n
    #n = int(input())
    n = 10

    #% Lista de datos
    #blocks = list(map(int, input().split()))
    #blocks = [4,3,2,2,2,1,3,3]
    blocks = [1000000842,1000000721,1000000671,1000000663,1000000626,1000000520,1000000126,999999978,1000000266,1000000501]
    #blocks = [4, 3, 2, 1, 3, 4]

    #% Llamar funcion
    estado = verificar(blocks,n)
    print(estado)

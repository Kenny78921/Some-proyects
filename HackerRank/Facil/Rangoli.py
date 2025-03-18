
#% https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

def print_rangoli(size):
    largo = int(size*2-1)
    ancho = int((size-1)*4+1)
    num_letras = int(largo / 2)
    
    lista_I = []
    lista_D = []

    
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    abecedario_recortado = abecedario[0:num_letras+1]
    abecedario_recortado.reverse()
    
    valor_x_1 = 0
    
    for x in range(largo):
        if valor_x_1 == 0 and largo !=1:
            lista_I.append(abecedario_recortado[x])
            
            cadena_letras = "-".join(lista_I)
            print(f"{cadena_letras}".center(ancho, "-"))
            
        if valor_x_1 < num_letras and valor_x_1 != 0 and largo!=1:
            lista_I.append(abecedario_recortado[x])
            lista_D.insert(0,abecedario_recortado[x-1])
            
            cadena_letras = "-".join(lista_I+lista_D)
            
            print(f"{cadena_letras}".center(ancho, "-"))
            
        if valor_x_1 == num_letras and largo!=1 :
            lista_I.append(abecedario_recortado[x])
            lista_D.insert(0,abecedario_recortado[x-1])
            
            cadena_letras = "-".join(lista_I+lista_D)
            
            print(f"{cadena_letras}".center(ancho, "-"))
            
            
        if valor_x_1 > num_letras and valor_x_1!= largo-1 and largo!=1:
            lista_I.pop(-1)
            lista_D.pop(0)
            cadena_letras = "-".join(lista_I+lista_D)
            
            print(f"{cadena_letras}".center(ancho, "-"))
            
        if valor_x_1 == largo-1 and largo!=1:
            lista_I.pop(-1)
            
            cadena_letras = "-".join(lista_I)
            
            print(f"{cadena_letras}".center(ancho, "-"))
        
        if largo==1:
            lista_I.append(abecedario_recortado[x])      
            print(f"{lista_I[0]}")
        valor_x_1+=1
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#% https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

import cmath
import re

r = str(input())
lista_r = list(map(int,(re.findall(r".?\d+",r))))

distancia = abs(complex(lista_r[0], lista_r[1]))
angulo = cmath.phase(complex(lista_r[0], lista_r[1]))

print(distancia)
print(angulo)
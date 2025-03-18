
#% https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true

import re

# Funcion remove
def remove():
    pass
    
# Entradas de datos
lines = int(input())

for x in range(lines):
    text = input()
    print(re.sub(r"(?<=\s)(&&)(?=\s)","and",re.sub(r"(?<=\s)(\|\|)(?=\s)","or"
    ,text)))
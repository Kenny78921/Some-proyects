
#% https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true

import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
texto = ""
for _ in range(n):
    matrix_item = list(input())
    matrix.append(matrix_item)

for a in range(m):
    for b in range(n):
        texto += matrix[b][a]

print(re.sub(r"(?<=[A-Z-a-z-0-9])[!,@,#,$,%,&, ]+(?=[A-Z-a-z-0-9])", " ", texto))


A = map(int, input().split(" "))
A = list(A)
A.sort()

B = map(int, input().split(" "))
B = list(B)
B.sort()

print(A, end=",")
print(B, end=",")
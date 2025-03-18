nums = [10, 20, 21, 22, 23, 30, 31, 32, 33, 34, 35]
nums = set(nums)

current_l = []
max_l = []

for x in range(min(nums), max(nums)+1):
    #3 Verifica si el numero actual se encuentra en el set
    if x in nums:
        #3 Añada el numero a la lista
        current_l.append(x)
    else:
        if len(current_l) > len(max_l):
            max_l = current_l.copy()
        current_l = []
    if x == max(nums):
        if len(current_l) > len(max_l):
            max_l = current_l.copy()

print(max_l)
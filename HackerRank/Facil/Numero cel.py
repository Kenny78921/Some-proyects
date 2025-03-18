import re
for x in range(int(input())):
    number = input()
    match = re.match(r"^[7-9][0-9]{9}$", number)

    if match:
        print("YES")
    else:
        print("NO")
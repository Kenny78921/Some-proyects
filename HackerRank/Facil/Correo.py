
#% https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true

import re

for x in range(9):
    email = input().split()

    match = re.search(r"<[a-zA-Z][a-zA-Z0-9-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>", email[1])

    try: 
        print("Es esteeeeeeeeeeeeeeeeeeeee: ", email[0], match.group())
    except AttributeError as e:
        pass
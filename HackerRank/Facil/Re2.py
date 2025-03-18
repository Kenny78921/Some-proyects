
#% https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true

import re

S = input().strip()
k = input().strip()

pattern = r'(?={})'.format(re.escape(k))
matches = list(re.finditer(pattern, S))

if matches:
    for m in matches:
        print((m.start(), m.start() + len(k) - 1))
else:
    print((-1, -1))
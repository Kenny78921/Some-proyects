
#% https://www.hackerrank.com/challenges/validate-a-roman-number/problem?isFullScreen=true

regex_pattern = r"^(?!.*([CDXIMDV])\1{3,})(?!.*LL).*$"

import re
print(str(bool(re.match(regex_pattern, input()))))
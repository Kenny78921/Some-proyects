
#% https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true

import re

code_lines = int(input())

for x in range(code_lines):
    text = input()
    matches = re.findall(r"(?<=.)(#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6})(?=;)",text)
    if matches:
        for i in matches:
            print(i)
import re

n = int(input())
inside_block = False

for _ in range(n):
    line = input()

    if '{' in line:
        inside_block = True
        continue
    if '}' in line:
        inside_block = False
        continue

    if inside_block:
        colors = re.findall(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b', line)
        for color in colors:
            print(color)

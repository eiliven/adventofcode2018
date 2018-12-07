from functools import reduce

with open('input.txt') as f:
    content = f.readlines()

s = reduce((lambda x, y: x + int(y)), [0] + content)
print(s)

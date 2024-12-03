import re

input = open("input.txt", "r").read()
multiplications = re.findall(r"mul\((\d{1,3})\,(\d{1,3})\)", input)
sum = sum([int(x) * int(y) for x, y in multiplications])

print(sum)

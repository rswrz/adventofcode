import re

input = open("input.txt", "r").read()
instructions = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)", input)

do = True
sum = 0

for instruction in instructions:
    if instruction == "don't()":
        do = False
    elif instruction == "do()":
        do = True
    elif do:
        a, b = re.findall(r"\d+", instruction)
        sum += int(a) * int(b)

print(sum)

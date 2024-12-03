from main import parse
import re


if __name__ == "__main__":
    input = parse("input.txt")

    sum = 0
    instructions = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)", input)

    do = True
    for instruction in instructions:
        if instruction == "don't()":
            do = False
        elif instruction == "do()":
            do = True
        elif do:
            x, y = re.findall(r"mul\((\d{1,3})\,(\d{1,3})\)", instruction)[0]
            sum += int(x) * int(y)

    print("Sum:", sum)

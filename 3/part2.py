from main import parse
import re


if __name__ == "__main__":
    input = parse("input.txt")

    sum = 0
    instructions = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)", input)

    do = True
    multiplications = []
    for instruction in instructions:
        if instruction == "don't()":
            do = False
        elif instruction == "do()":
            do = True
        elif do:
            multiplications += re.findall(r"mul\((\d{1,3})\,(\d{1,3})\)", instruction)

    for multiplication in multiplications:
        product = int(multiplication[0]) * int(multiplication[1])
        sum += product

    print("Sum:", sum)

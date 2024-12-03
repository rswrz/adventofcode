import re


def parse(input):
    with open(input, "r") as file:
        memory = file.read()
    return memory


if __name__ == "__main__":
    input = parse("input.txt")

    sum = 0
    multiplications = re.findall(r"mul\((\d{1,3})\,(\d{1,3})\)", input)

    for multiplication in multiplications:
        product = int(multiplication[0]) * int(multiplication[1])
        sum += product

    print("Sum:", sum)

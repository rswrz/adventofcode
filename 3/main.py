import re


def parse(input):
    memory = []
    with open(input, "r") as file:
        for line in file:
            memory.append(line)
    return memory


if __name__ == "__main__":
    input = parse("input.txt")

    sum = 0
    for line in input:
        multiplications = re.findall(r"mul\((\d{1,3})\,(\d{1,3})\)", line)

        for multiplication in multiplications:
            product = int(multiplication[0]) * int(multiplication[1])
            sum += product

    print("Sum:", sum)  # 173529487

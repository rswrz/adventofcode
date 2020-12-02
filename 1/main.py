def parse(input):
    pairs = []
    with open(input, "r") as file:
        for line in file:
            numbers = [int(word) for word in line.split() if word.isdigit()]
            pairs.append(numbers)
    return pairs

if __name__ == "__main__":
    input = parse("input.txt")
    print("Input:", input)

    left = [pair[0] for pair in input]
    right = [pair[1] for pair in input]
    sorted = list(zip(sorted(left), sorted(right)))
    print("Sorted input:", sorted)

    distances = [abs(pair[0] - pair[1]) for pair in sorted]
    print("Distances:", distances)

    distance = sum(distances)
    print("Distance:", distance)

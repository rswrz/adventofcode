def parse(input):
    pairs = []
    with open(input, "r") as file:
        for line in file:
            numbers = [int(word) for word in line.split() if word.isdigit()]
            pairs.append(numbers)
    return pairs


if __name__ == "__main__":
    input = parse("input.txt")

    left = [pair[0] for pair in input]
    right = [pair[1] for pair in input]

    sorted_pairs = list(zip(sorted(left), sorted(right)))

    distances = [abs(pair[0] - pair[1]) for pair in sorted_pairs]
    distance = sum(distances)

    print("Distance:", distance)

from main import parse

if __name__ == "__main__":
    input = parse("input.txt")
    print("Input:", input)

    left = [pair[0] for pair in input]
    right = [pair[1] for pair in input]

    similarities = []

    for id_left in left:
        i = 0
        for id_right in right:
            if id_left == id_right:
                i += 1
        print("Location ID", id_left, "found", i, "times")
        similarities.append(id_left * i)

    print("Similarities:", similarities)

    print("Similarity Score:", sum(similarities))

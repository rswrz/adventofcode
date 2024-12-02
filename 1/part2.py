from main import parse

if __name__ == "__main__":
    input = parse("input.txt")

    left = [pair[0] for pair in input]
    right = [pair[1] for pair in input]

    similarities = []

    for id_left in left:
        counter = 0
        for id_right in right:
            if id_left == id_right:
                counter += 1
        similarities.append(id_left * counter)

    print("Similarity Score:", sum(similarities))

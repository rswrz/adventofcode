input = open("input.txt").read().splitlines()
data = [list(row) for row in input]

X_coordinates = []
for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == "X":
            X_coordinates.append([x, y])

count = 0
max = len(data) - 1

for x, y in X_coordinates:
    XMAS = {
        "right": "".join([data[y][x], data[y][x + 1], data[y][x + 2], data[y][x + 3]]) if x + 3 <= max else None,
        "left": "".join([data[y][x], data[y][x - 1], data[y][x - 2], data[y][x - 3]]) if x - 3 >= 0 else None,
        "up": "".join([data[y][x], data[y - 1][x], data[y - 2][x], data[y - 3][x]]) if y - 3 >= 0 else None,
        "down": "".join([data[y][x], data[y + 1][x], data[y + 2][x], data[y + 3][x]]) if y + 3 <= max else None,
        "right_down": "".join([data[y][x], data[y + 1][x + 1], data[y + 2][x + 2], data[y + 3][x + 3]]) if x + 3 <= max >= y + 3 else None,
        "right_up": "".join([data[y][x], data[y - 1][x + 1], data[y - 2][x + 2], data[y - 3][x + 3]]) if x + 3 <= max and y - 3 >= 0 else None,
        "left_down": "".join([data[y][x], data[y + 1][x - 1], data[y + 2][x - 2], data[y + 3][x - 3]]) if x - 3 >= 0 and y + 3 <= max else None,
        "left_up": "".join([data[y][x], data[y - 1][x - 1], data[y - 2][x - 2], data[y - 3][x - 3]]) if x - 3 >= 0 <= y - 3 else None,
    }  # fmt: skip

    count += list(XMAS.values()).count("XMAS")

print(count)

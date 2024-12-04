input = open("input.txt").read().splitlines()
matrix = [list(row) for row in input]

a_coordinates = []
for y, row in enumerate(matrix):
    if y > 0 and y < len(matrix) - 1:
        for x, char in enumerate(row):
            if x > 0 and x < len(matrix) - 1:
                if char == "A":
                    a_coordinates.append((x, y))

count = 0
for a in a_coordinates:
    x, y = a

    l_top = matrix[y - 1][x - 1]
    l_bot = matrix[y + 1][x - 1]
    r_top = matrix[y - 1][x + 1]
    r_bot = matrix[y + 1][x + 1]

    if l_top == "M" and r_bot == "S" and l_bot == "M" and r_top == "S":
        count += 1
    elif l_top == "M" and r_bot == "S" and l_bot == "S" and r_top == "M":
        count += 1
    elif l_top == "S" and r_bot == "M" and l_bot == "M" and r_top == "S":
        count += 1
    elif l_top == "S" and r_bot == "M" and l_bot == "S" and r_top == "M":
        count += 1
print(count)

import re


def rotate_45_degrees_right(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[] for _ in range(n + m - 1)]

    for i in range(n):
        for j in range(m):
            result[i + j].append(matrix[j][i])

    return result


def rotate_45_degrees_left(matrix):
    n = len(matrix)
    m = len(matrix[0])
    max_index = m - 1
    result = [[] for _ in range(n + m - 1)]

    for i in range(n):
        for j in range(m):
            result[j - i + max_index].append(matrix[i][j])

    return list(reversed(result))


with open("input.txt") as file:
    input = file.read().splitlines()

print("--- INPUT ---")

for row in input:
    print(" ".join(row))

print("--- MATRIX ---")

matrix = [list(line) for line in input]
for row in matrix:
    print(" ".join(row))

print("--- ROTATE 90 LEFT ---")

rotated = list(reversed(list(zip(*matrix))))

for row in rotated:
    print(" ".join(row))

print("--- ROTATE 45 LEFT --- ")

rotated_45_left = rotate_45_degrees_left(matrix)
for row in rotated_45_left:
    print("  ".join(row).center(30))

print("--- ROTATE 45 RIGHT ---")

rotated_45_right = rotate_45_degrees_right(matrix)
for row in rotated_45_right:
    print("  ".join(row).center(30))

print("--- END DEBUG ---")

### COUNT

count = 0
# left + right
left_right_count = 0
for row in matrix:
    left_right_count += len(re.findall(r"(?=(XMAS|SAMX))", "".join(row)))
print("left + right", left_right_count)
count += left_right_count

# top + down
top_down_count = 0
for row in rotated:
    top_down_count += len(re.findall(r"(?=(XMAS|SAMX))", "".join(row)))
print("top + down", top_down_count)
count += top_down_count

# right-down + left-up
right_down_left_up_count = 0
for row in rotated_45_left:
    right_down_left_up_count += len(re.findall(r"(?=(XMAS|SAMX))", "".join(row)))
print("right-down + left-up", right_down_left_up_count)
count += right_down_left_up_count

# right-up + left-down
right_up_left_down_count = 0
for row in rotated_45_right:
    right_up_left_down_count += len(re.findall(r"(?=(XMAS|SAMX))", "".join(row)))
print("right-up + left-down", right_up_left_down_count)
count += right_up_left_down_count

print(count)

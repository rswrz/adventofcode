def parse(input):
    sequence = []
    with open(input, "r") as file:
        for line in file:
            numbers = [int(word) for word in line.split() if word.isdigit()]
            sequence.append(numbers)
    return sequence


def rule1(report):
    # Rule: The levels are either all increasing or all decreasing.
    return report == sorted(report) or report == sorted(report, reverse=True)


def rule2(report):
    # Rule: Any two adjacent levels differ by at least one and at most three.
    for i in range(len(report)):
        if i > 0:
            if abs(report[i] - report[i - 1]) not in range(1, 4):
                return False
    return True


if __name__ == "__main__":
    input = parse("input.txt")
    safe_reports_counter = 0

    for report in input:
        if rule1(report) and rule2(report):
            safe_reports_counter += 1

    print("Safe reports:", safe_reports_counter)

def parse(input):
    pairs = []
    with open(input, "r") as file:
        for line in file:
            numbers = [int(word) for word in line.split() if word.isdigit()]
            pairs.append(numbers)
    return pairs


def rule1(report, debug=False):
    report_sorted_inclemently = sorted(report)
    report_sorted_decremental = sorted(report, reverse=True)

    if debug:
        print("Report levels increasing:", report_sorted_inclemently)
        print("Report levels decreasing:", report_sorted_decremental)

    if report == report_sorted_inclemently or report == report_sorted_decremental:
        return True
    else:
        print("Report is unsafe because levels ar not all increasing or all decreasing")
        return False


def rule2(report, debug=False):
    for i, level in enumerate(report):
        if i == 0:
            continue
        else:
            curr_level = report[i]
            prev_level = report[i - 1]
            diff = abs(curr_level - prev_level)
            if debug:
                print("Level", curr_level, "to", prev_level, "diff is:", diff)
            if diff < 1 or diff > 3:
                print("Report is NOT safe! Validation of rule 2 failed!")
                print("Stopping validation!")
                return False
    return True


if __name__ == "__main__":
    input = parse("input.txt")
    print("Input:", input)

    count_reports = len(input)
    print("Number of reports:", count_reports)
    count_save_reports = 0

    for report in input:
        print("---\n")
        print("Report:", report)
        debug = True

        # Rule 1 - The levels are either all increasing or all decreasing.
        print("Validating rule 1...")
        if rule1(report, debug):
            print("Rule 1 passed successfully!")
        else:
            continue

        # Rule 2 - Any two adjacent levels differ by at least one and at most three.
        print("Validating rule 2...")
        if rule2(report, debug):
            print("Rule 2 passed successfully!")
        else:
            continue

        # Increment save reports count
        print("Report is safe, all rules passed successfully.")
        count_save_reports += 1

    print("---\n")
    print("Total reports:", count_reports)
    print("Save reports:", count_save_reports)

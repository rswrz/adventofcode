from main import parse, rule1, rule2


def validate_rules(report, tolerate=False):
    if rule1(report) and rule2(report):
        return True

    if tolerate:
        for i in range(len(report)):
            if validate_rules([level for j, level in enumerate(report) if j != i]):
                return True


if __name__ == "__main__":
    input = parse("input.txt")
    safe_reports_counter = 0

    for report in input:
        if validate_rules(report, tolerate=True):
            safe_reports_counter += 1

    print("Safe reports:", safe_reports_counter)

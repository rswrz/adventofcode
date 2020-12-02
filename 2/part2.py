from main import parse, rule1, rule2

def validate_rules(report, debug=False):
    if rule1(report, debug):
        if rule2(report, debug):
            return True

    for i in range(len(report)):
        tolerated_report = report.copy()
        tolerated_report.pop(i)
        if rule1(tolerated_report, debug):
            if rule2(tolerated_report, debug):
                return True

    return False


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

        if validate_rules(report, debug):
            print("Valid!")
        else:
            # Invalid report, do not count
            continue

        # Increment save reports count
        print("Report is safe, all rules passed successfully.")
        count_save_reports += 1

    print("---\n")
    print("Total reports:", count_reports)
    print("Save reports:", count_save_reports)

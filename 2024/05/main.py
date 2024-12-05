def valid_page_order(update, rules):
    for i, page in enumerate(update):
        for before, after in rules:
            if (
                page == before
                and i > update.index(after)
                or page == after
                and i < update.index(before)
            ):
                return False
    return True


input = open("input.txt").read().splitlines()
rules = [list(map(int, line.split("|"))) for line in input if "|" in line]
updates = [list(map(int, line.split(","))) for line in input if "," in line]

result = 0
for update in updates:
    update_rules = [rule for rule in rules if all(r in update for r in rule)]

    if valid_page_order(update, update_rules):
        middle_page_index = int((len(update) - 1) / 2)
        result += update[middle_page_index]

print(result)

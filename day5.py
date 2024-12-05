TEST = False

def get_input():
    input_file = "input/day5.txt"
    if TEST:
        input_file = "input/day5_test.txt"

    with open(input_file) as fd:
        lines = fd.readlines()
    return lines


def parse(lines: list[str]):
    rules = []
    updates = []
    for line in lines:
        if "|" in line:
            rules.append(line.strip().split("|"))
        elif "," in line:
            updates.append(line.strip().split(","))
    return rules, updates


def correct_order(update: list, rules: list):
    for rule in rules:
        if rule[0] not in update or rule[1] not in update:
            continue

        # check rule is followed
        left_idx = update.index(rule[0])
        right_idx = update.index(rule[1])
        if left_idx > right_idx:
            return False
    return True


def main():
    lines = get_input()

    rules, updates = parse(lines)

    # ---PART 1 ---------------------
    part1_solution = 0

    for update in updates:
        if correct_order(update, rules):
            part1_solution += int(update[len(update)//2])

    print("Part 1: ", part1_solution)


    # ---PART 2 ---------------------
    part2_solution = 0

    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

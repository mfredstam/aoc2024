TEST = False

def get_input():
    input_file = "input/day2.txt"
    if TEST:
        input_file = "input/day2_test.txt"

    with open(input_file) as fd:
        lines = fd.readlines()
    return lines


def check_diff(level: list, min=1, max=3) -> bool:
    for idx in range(0, len(level)):
        if idx+1 == len(level):
            break
        if not (min <= abs(level[idx] - level[idx+1]) <= max):
            return False
    return True


def main():
    reports = get_input()

    # ---PART 1 ---------------------
    part1_solution = 0
    for report in reports:
        levels = report.split(" ")
        levels = list(map(int, levels))

        incr_or_decr_ok = sorted(levels) == levels or sorted(levels, reverse=True) == levels
        diff_ok = check_diff(levels)
        if incr_or_decr_ok and diff_ok:
            part1_solution += 1

    print("Part 1: ", part1_solution)


    # ---PART 2 ---------------------
    part2_solution = 0

    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

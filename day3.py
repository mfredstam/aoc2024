import re

TEST = False


def get_input():
    input_file = "input/day3.txt"
    if TEST:
        input_file = "input/day3_test.txt"

    with open(input_file) as fd:
        lines = fd.readlines()
    return lines

re_mul = re.compile("mul\((?P<a>\d{1,3})\,(?P<b>\d{1,3})\)")
re_enable = re.compile("do\(\)")
re_disable = re.compile("don\'t\(\)")


def calc_do_ranges(enable_pos: list, disable_pos: list) -> list:
    do_ranges = []
    for e_pos in enable_pos:
        for d_pos in disable_pos:
            if e_pos < d_pos:
                do_ranges.append(range(e_pos, d_pos))
                break
    return do_ranges


def main():
    lines = get_input()

    # ---PART 1 ---------------------
    part1_solution = 0
    for line in lines:
        for match in re_mul.findall(line):
            part1_solution += int(match[0]) * int(match[1])

    print("Part 1: ", part1_solution)


    # ---PART 2 ---------------------
    part2_solution = 0

    do_positions = [0]  # Enabled at start
    dont_positions = []

    # Make all lines into one line without newline
    line = ""
    for x in lines:
        line += x.strip()

    # Find all "do()" and "don't()"
    for enable_match in re_enable.finditer(line):
        do_positions.append(enable_match.start())
    for disable_match in re_disable.finditer(line):
        dont_positions.append(disable_match.start())

    # Calculate the ranges that are enabled
    do_ranges = calc_do_ranges(do_positions, dont_positions)

    for match in re_mul.finditer(line):
        for do_range in do_ranges:
            if match.start() in do_range:
                part2_solution += int(match.group(1)) * int(match.group(2))
                break

    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

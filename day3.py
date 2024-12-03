import re
from pprint import pprint

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

def calc_enabled_ranges(enable_pos, disable_pos):
    enabled_ranges = []
    for e_pos in enable_pos:
        prev_d_pos = None
        for d_pos in reversed(disable_pos):
            if e_pos > d_pos or (e_pos == enable_pos[-1] and d_pos == disable_pos[-1]):
                if prev_d_pos:
                    enabled_ranges.append(range(e_pos, prev_d_pos))
                else:
                    enabled_ranges.append(range(e_pos, d_pos))
                break
            prev_d_pos = d_pos
    enabled_ranges.insert(0, range(0, disable_pos[0]))  # Enabled by default
    pprint(enabled_ranges)
    return enabled_ranges

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

    enable_pos = [0]
    disable_pos = []

    for line in lines:
        for enable_match in re_enable.finditer(line):
            enable_pos.append(enable_match.end())
        for disable_match in re_disable.finditer(line):
            disable_pos.append(disable_match.end())

    enabled_ranges = calc_enabled_ranges(enable_pos, disable_pos)

    for line in lines:
        for match in re_mul.finditer(line):
            for enabled_range in enabled_ranges:
                if match.start() in enabled_range:
                    #print("Enabled pos: ", match.group(0))
                    part2_solution += int(match.group(1)) * int(match.group(2))
                    break

    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

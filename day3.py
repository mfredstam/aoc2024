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

    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

TEST = True

def get_input():
    input_file = "input/dayX.txt"
    if TEST:
        input_file = "input/dayX_test.txt"

    with open(input_file) as fd:
        lines = fd.readlines()
    return lines


def main():
    lines = get_input()

    # ---PART 1 ---------------------
    part1_solution = 0

    print("Part 1: ", part1_solution)


    # ---PART 2 ---------------------
    part2_solution = 0

    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

import itertools

TEST = False

def get_input():
    input_file = "input/day7.txt"
    if TEST:
        input_file = "input/day7_test.txt"

    with open(input_file) as fd:
        lines = fd.readlines()
    return lines


def parse(lines: list) -> dict:
    equations = []
    for line in lines:
        test_value, nums = line.strip().split(": ")
        equations.append((int(test_value), [int(x) for x in nums.split(" ")]))
    return equations


def generate_combinations(N) -> list:
    operators = ['+', '*']
    combinations = itertools.product(operators, repeat=N)
    return [''.join(comb) for comb in combinations]


def apply_combination(test_value, nums, combinations) -> int:
    for combination in combinations:
        expr = nums[0]
        for comb, n in zip(combination, nums[1:]):
            if comb == "+":
                expr = expr + n
            elif comb == "*":
                expr = expr * n
        if test_value == expr:
            return test_value
    return 0


def evaluate(equations: list) -> int:
    total_calibration_result = 0

    for test_value, nums in equations:
        combinations = generate_combinations(len(nums) - 1)
        assert len(combinations) == 2**(len(nums) - 1)

        total_calibration_result += apply_combination(test_value, nums, combinations)

    return total_calibration_result


def main():
    lines = get_input()
    equations = parse(lines)

    # ---PART 1 ---------------------
    part1_solution = 0

    part1_solution = evaluate(equations)

    print("Part 1: ", part1_solution)


    # ---PART 2 ---------------------
    part2_solution = 0

    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

TEST = False

def get_input():
    input_file = "input/day4.txt"
    if TEST:
        input_file = "input/day4_test.txt"

    with open(input_file) as fd:
        lines = fd.readlines()
    return lines


def create_matrix(lines: list) -> dict:
    matrix = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            matrix[(x, y)] = c
    return matrix, x, y


def check_dir(matrix, pos_to_check) -> bool:
    values = ["X", "M", "A", "S",]
    try:
        for pos, value in zip(pos_to_check, values):
            if matrix[pos] != value:
                return False
    except KeyError:
        return False
    return True


def check_surrounding(matrix, row, col) -> int:
    direction_positions = [
        [(row, col), (row+1, col), (row+2, col), (row+3, col),],
        [(row, col), (row-1, col), (row-2, col), (row-3, col),],
        [(row, col), (row, col+1), (row, col+2), (row, col+3),],
        [(row, col), (row, col-1), (row, col-2), (row, col-3),],
        # Diagonal
        [(row, col), (row-1, col-1), (row-2, col-2), (row-3, col-3),],
        [(row, col), (row-1, col+1), (row-2, col+2), (row-3, col+3),],
        [(row, col), (row+1, col-1), (row+2, col-2), (row+3, col-3),],
        [(row, col), (row+1, col+1), (row+2, col+2), (row+3, col+3),],
    ]
    no_xmas = 0
    for dir_pos in direction_positions:
        if check_dir(matrix, dir_pos):
            no_xmas += 1
    return no_xmas


def check_surrounding_mas(matrix, row, col):
    direction_positions = [
        (row-1, col-1),
        (row+1, col+1),
        (row+1, col-1),
        (row-1, col+1),
    ]

    for dir_pos in direction_positions:
        if matrix[dir_pos] not in "MS":
            return 0

    # Check that diagnoal is M and S
    if (matrix[(row-1, col-1)] == "M" and matrix[(row+1, col+1)] == "M") \
        or (matrix[(row-1, col-1)] == "S" and matrix[(row+1, col+1)] == "S") \
        or (matrix[(row-1, col+1)] == "M" and matrix[(row+1, col-1)] == "M") \
        or (matrix[(row-1, col+1)] == "S" and matrix[(row+1, col-1)] == "S"):
        return 0

    return 1


def main():
    lines = get_input()

    matrix, rows, cols = create_matrix(lines)

    # ---PART 1 ---------------------
    part1_solution = 0

    for row in range(0, rows+1):
        for col in range(0, cols+1):
            if matrix[(row, col)] == "X":
                part1_solution += check_surrounding(matrix, row, col)

    print("Part 1: ", part1_solution)


    # ---PART 2 ---------------------
    part2_solution = 0

    for row in range(1, rows):
        for col in range(1, cols):
            if matrix[(row, col)] == "A":
                part2_solution += check_surrounding_mas(matrix, row, col)

    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

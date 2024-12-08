from pprint import pprint

TEST = False


DIR_UP = 0
DIR_RIGHT = 1
DIR_DOWN = 2
DIR_LEFT = 3


def get_input():
    input_file = "input/day6.txt"
    if TEST:
        input_file = "input/day6_test.txt"

    with open(input_file) as fd:
        lines = fd.readlines()
    return lines


def parse(lines: list):
    matrix = {}
    start_pos = None
    for row, line in enumerate(lines):
        for col, c in enumerate(line.strip()):
            if c == "^":
                start_pos = (row, col)
            matrix[(row, col)] = c
    return matrix, start_pos


def peek_next_pos(current_pos, direction) -> tuple:
    next_pos = [0, 0]
    next_pos[0] = current_pos[0]
    next_pos[1] = current_pos[1]
    if direction == DIR_UP:
        next_pos[0] = next_pos[0] - 1
    elif direction == DIR_DOWN:
        next_pos[0] = next_pos[0] + 1
    elif direction == DIR_LEFT:
        next_pos[1] = next_pos[1] - 1
    elif direction == DIR_RIGHT:
        next_pos[1] = next_pos[1] + 1
    return tuple(next_pos)


def move(current_pos, direction) -> None:
    if direction == DIR_UP:
        current_pos[0] = current_pos[0] - 1
    elif direction == DIR_DOWN:
        current_pos[0] = current_pos[0] + 1
    elif direction == DIR_LEFT:
        current_pos[1] = current_pos[1] - 1
    elif direction == DIR_RIGHT:
        current_pos[1] = current_pos[1] + 1


def change_direction(current_direction):
    current_direction = (current_direction + 1) % 4
    return current_direction


def walk(matrix: dict, start_pos: tuple, direction: int) -> int:
    distinct_positions = []
    in_area = True
    current_pos = list(start_pos)
    distinct_positions.append(tuple(current_pos))

    while in_area:
        next_pos = peek_next_pos(current_pos, direction)
        try:
            if matrix[tuple(next_pos)] == "#":
                direction = change_direction(direction)
            else:
                move(current_pos, direction)
                distinct_positions.append(tuple(current_pos))
        except KeyError:
            in_area = False
    return len(set(distinct_positions))


def walk_2(matrix: dict, start_pos: tuple, direction: int) -> int:
    distinct_positions = []
    in_area = True
    current_pos = list(start_pos)
    distinct_positions.append(tuple(current_pos))

    while in_area:
        next_pos = peek_next_pos(current_pos, direction)
        try:
            if matrix[tuple(next_pos)] == "#":
                direction = change_direction(direction)
            else:
                move(current_pos, direction)
                distinct_positions.append(tuple(current_pos))
                if len(distinct_positions) > 10000:
                    return True
        except KeyError:
            in_area = False
    return False


def walk_with_obstruction(matrix: dict, start_pos: tuple, direction: int) -> int:
    num_of_loops = 0
    for pos, c in matrix.items():
        if c == ".":
            matrix[pos] = "#"
            if walk_2(matrix, start_pos, direction):
                num_of_loops += 1
            matrix[pos] = "."
    return num_of_loops


def main():
    lines = get_input()
    matrix, start_pos = parse(lines)
    current_dir = DIR_UP

    # ---PART 1 ---------------------
    part1_solution = 0

    part1_solution = walk(matrix, start_pos, current_dir)

    print("Part 1: ", part1_solution)


    # ---PART 2 ---------------------
    part2_solution = 0

    part2_solution = walk_with_obstruction(matrix, start_pos, current_dir)

    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

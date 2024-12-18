import heapq

TEST = False

def get_input():
    input_file = "input/day18.txt"
    if TEST:
        input_file = "input/day18_test.txt"

    with open(input_file) as fd:
        lines = fd.readlines()
    return lines


def parse(lines: list, n: int=1024) -> dict:
    grid = {}
    if TEST:
        g = 7
    else:
        g = 71
    for x in range(0, g):
        for y in range(0, g):
            grid[(x, y)] = "."

    prev_coord = None
    for i, coord in enumerate(lines):
        if i >= n:
            break
        x, y = coord.strip().split(",")
        grid[(int(y), int(x))] = "#"
        prev_coord = coord
    
    return grid, prev_coord


def solve(grid: dict) -> int:
    start = (0, 0)
    if TEST:
        end = (6, 6)
    else:
        end = (70, 70)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    # Priority queue to hold (cost, row, col, path)
    pq = [(0, start[0], start[1], [start])]
    visited = set()

    while pq:
        cost, row, col, path = heapq.heappop(pq)

        # If the cell is already visited, skip it
        if (row, col) in visited:
            continue
        visited.add((row, col))

        # If we reach the end, return the cost and path
        if (row, col) == end:
            return cost, path

        # Explore neighbors
        for dr, dc in directions:
            r, c = row + dr, col + dc

            if (r, c) in grid and grid[(r, c)] == "." and (r, c) not in visited:
                heapq.heappush(pq, (cost + 1, r, c, path + [(r, c)]))
    return -1, []

def main():
    lines = get_input()
    if TEST:
        grid, _ = parse(lines, n=12)
    else:
        grid, _ = parse(lines, n=1024)

    # ---PART 1 ---------------------
    part1_solution = 0

    part1_solution, path = solve(grid)

    print("Part 1: ", part1_solution)


    # ---PART 2 ---------------------
    part2_solution = 0

    if TEST:
        s = 12
        e = 25
    else:
        s = 1024
        e = 3450

    for i in range(s, e):
        grid, coord = parse(lines, n=i)

        part2_solution, path = solve(grid)

        if part2_solution == -1:
            part2_solution = coord
            break


    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

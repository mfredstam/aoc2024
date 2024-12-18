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
    for x in range(0, 71):
        for y in range(0, 71):
            grid[(x, y)] = "."

    for i, coord in enumerate(lines):
        if i >= n:
            break
        x, y = coord.strip().split(",")
        grid[(int(y), int(x))] = "#"
    
    return grid


def solve(grid: dict, start: tuple, end: tuple) -> int:
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
    return float('inf'), []

def main():
    lines = get_input()
    if TEST:
        grid = parse(lines, n=12)
    else:
        grid = parse(lines, n=1024)

    # ---PART 1 ---------------------
    part1_solution = 0

    start = (0, 0)
    if TEST:
        end = (6, 6)
    else:
        end = (70, 70)
    part1_solution, path = solve(grid, start, end)

    print("Part 1: ", part1_solution)


    # ---PART 2 ---------------------
    part2_solution = 0

    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

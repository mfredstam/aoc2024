TEST = False

def get_input():
    input_file = "input/day11.txt"
    if TEST:
        input_file = "input/day11_test.txt"

    with open(input_file) as fd:
        lines = fd.readlines()
    return lines


def parse(line: str) -> list:
    stones = line.split(" ")
    stones = [int(s) for s in stones]
    return stones


def blink(stones: list, n: int) -> int:
    # lookup = {0: (1,)}
    new_stones = []
    temp_stones = stones[:]
    for i in range(0, n):
        x = []
        for stone in temp_stones:
            if stone == 0:
                x.append(1)
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                a = int(s[:len(s)//2])
                b = int(s[len(s)//2:])
                x.append(a)
                x.append(b)
            else:
                x.append(stone * 2024)
        temp_stones = x[:]
        new_stones = temp_stones[:]
    return len(new_stones)

def main():
    line = get_input()[0].strip()

    stones = parse(line)

    # ---PART 1 ---------------------
    part1_solution = 0

    part1_solution = blink(stones, n=25)

    print("Part 1: ", part1_solution)


    # ---PART 2 ---------------------
    part2_solution = 0

    part2_solution = blink(stones, n=75)

    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

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


def to_dict_counter(stones: list) -> dict:
    a = {}
    for stone in stones:
        try:
            a[stone] += 1
        except KeyError:
            a[stone] = 1
    return a


def blink_2(stones: dict, n: int) -> int:
    for i in range(0, n):
        temp_stones = {}
        for k, v in stones.items():
            if k == 0:
                try:
                    temp_stones[1] += v
                except KeyError:
                    temp_stones[1] = v
            elif len(str(k)) % 2 == 0:
                s = str(k)
                a = int(s[:len(s)//2])
                b = int(s[len(s)//2:])
                try:
                    temp_stones[a] += v
                except KeyError:
                    temp_stones[a] = v
                try:
                    temp_stones[b] += v
                except KeyError:
                    temp_stones[b] = v
            else:
                try:
                    temp_stones[k * 2024] += v
                except KeyError:
                    temp_stones[k * 2024] = v
        stones = temp_stones
    return sum(stones.values())


def main():
    line = get_input()[0].strip()

    stones = parse(line)

    # ---PART 1 ---------------------
    part1_solution = 0

    part1_solution = blink(stones, n=25)

    print("Part 1: ", part1_solution)


    # ---PART 2 ---------------------
    part2_solution = 0

    stones = to_dict_counter(stones)

    part2_solution = blink_2(stones, n=75)

    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

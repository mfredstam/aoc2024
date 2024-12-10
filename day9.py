TEST = False


def get_input():
    input_file = "input/day9.txt"
    if TEST:
        input_file = "input/day9_test.txt"

    with open(input_file) as fd:
        lines = fd.readlines()
    return lines


def parse(disk_map: str) -> list:
    disk = []
    id_value = 0
    for i, c in enumerate(disk_map):
        if i % 2 == 0:  # File size
            for _ in range(0, int(c)):
                disk.append((id_value,))
            id_value += 1
        else:  # Free space
            for _ in range(0, int(c)):
                disk.append((".",))
    return disk


def defrag_disk(disk: list) -> list:
    for i, x in enumerate(reversed(disk), start=1):
        if x[0] == ".":
            continue

        left_most_free_idx = disk.index((".",))

        if left_most_free_idx > (len(disk) - i):
            break

        disk[left_most_free_idx], disk[len(disk)-i] = disk[len(disk)-i], disk[left_most_free_idx]

    return disk


def calc_checksum(disk: list) -> int:
    sum = 0
    for i, c in enumerate(disk):
        if c[0] == ".":
            break
        sum += (i * c[0])
    return sum


def calculate_checksum(disk_map: str) -> int:
    disk = parse(disk_map)
    disk = defrag_disk(disk)
    checksum = calc_checksum(disk)
    return checksum


def main():
    disk_map = get_input()[0].strip()

    # ---PART 1 ---------------------
    part1_solution = 0

    part1_solution = calculate_checksum(disk_map)

    print("Part 1: ", part1_solution)


    # ---PART 2 ---------------------
    part2_solution = 0

    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

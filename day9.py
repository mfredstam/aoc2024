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


def defrag_disk_full_file(disk: list) -> list:
    prev_id = -1
    for i, x in enumerate(reversed(disk), start=1):
        if x[0] == ".":
            continue

        current_id = x[0]
        if current_id == prev_id:
            continue

        right_most_file_idx = len(disk) - i
        left_most_file_idx = right_most_file_idx
        while disk[left_most_file_idx-1][0] == disk[right_most_file_idx][0]:
            left_most_file_idx -= 1

        file_size = right_most_file_idx - left_most_file_idx + 1

        free_size = 0
        right_most_free_idx = 0

        while file_size > free_size:
            try:
                left_most_free_idx = disk.index((".",), right_most_free_idx+1, left_most_file_idx+1)
            except ValueError:
                prev_id = current_id
                break
            right_most_free_idx = left_most_free_idx
            while disk[right_most_free_idx + 1][0] == ".":
                right_most_free_idx += 1
            free_size = right_most_free_idx - left_most_free_idx + 1


        if current_id != prev_id:
            for i in range(0, file_size):
                disk[left_most_free_idx+i], disk[left_most_file_idx+i] = disk[left_most_file_idx+i], disk[left_most_free_idx+i]

    return disk


def calc_checksum(disk: list) -> int:
    sum = 0
    for i, c in enumerate(disk):
        if c[0] == ".":
            continue
        sum += (i * c[0])
    return sum


def calculate_checksum(disk_map: str, full_file=False) -> int:
    disk = parse(disk_map)
    if full_file:
        disk = defrag_disk_full_file(disk)
    else:
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

    part2_solution = calculate_checksum(disk_map, full_file=True)

    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

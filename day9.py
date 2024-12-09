TEST = True

def get_input():
    input_file = "input/day9.txt"
    if TEST:
        input_file = "input/day9_test.txt"

    with open(input_file) as fd:
        lines = fd.readlines()
    return lines


def get_id_format(disk_map: str) -> str:
    id_format = ""
    file_size = True
    for id, c in enumerate(disk_map):
        if file_size:
            id_format = id_format + (str(id//2) * int(c))
            file_size = False
        else:
            id_format = id_format + ("." * int(c))
            file_size = True
    return id_format


def defrag(id_format: str) -> str:

    tester = [
        # "00...111...2...333.44.5555.6666.777.888899",
        "009..111...2...333.44.5555.6666.777.88889.",
        "0099.111...2...333.44.5555.6666.777.8888..",
        "00998111...2...333.44.5555.6666.777.888...",
        "009981118..2...333.44.5555.6666.777.88....",
        "0099811188.2...333.44.5555.6666.777.8.....",
        "009981118882...333.44.5555.6666.777.......",
        "0099811188827..333.44.5555.6666.77........",
        "00998111888277.333.44.5555.6666.7.........",
        "009981118882777333.44.5555.6666...........",
        "009981118882777333644.5555.666............",
        "00998111888277733364465555.66.............",
        "0099811188827773336446555566..............",
    ]

    x = 0
    for idx, c in enumerate(reversed(id_format)):
        if c == ".":
            x += 1
            continue
        x += 1
        free_idx = id_format.index(".")

        if free_idx >= (len(id_format) - idx):
            break

        id_format = id_format[:free_idx] + c + id_format[free_idx+1:-x] + "."*x


        # print(idx, ":  ", id_format, sep="")

        # if id_format != tester[x-1]:
        #     print("### CUR: ", id_format, "\n", "### COR: ", tester[x], sep="")
        #     raise ValueError

    return id_format


def calc_checksum(disk: str) -> int:
    sum = 0
    for i, c in enumerate(disk):
        if c == ".":
            break
        sum += (i * int(c))
    return sum

def calculate_checksum(disk_map: str) -> int:
    id_format = get_id_format(disk_map)
    # print(id_format)
    defragged_disk = defrag(id_format)
    print(defragged_disk)
    # assert defragged_disk == "0099811188827773336446555566.............."
    checksum = calc_checksum(defragged_disk)
    return checksum

def main():
    disk_map = get_input()[0].strip()

    # ---PART 1 ---------------------
    part1_solution = 0

    part1_solution = calculate_checksum(disk_map)

    low = 90428939430

    print("Part 1: ", part1_solution)


    # ---PART 2 ---------------------
    part2_solution = 0

    print("Part 2: ", part2_solution)


if __name__ == "__main__":
    main()

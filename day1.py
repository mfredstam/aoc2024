

def main():
    with open("input/day1.txt") as fd:
        lines = fd.readlines()

    right_list = []
    left_list = []

    for line in lines:
        a, b = line.split("   ")
        a, b = int(a), int(b)
        right_list.append(a)
        left_list.append(b)

    diff_dist = []

    for a, b in zip(sorted(right_list), sorted(left_list)):
        diff_dist.append(max(a, b) - min(a, b))

    print("Part 1: ", sum(diff_dist))


    translation = {}  # Lookup table
    lvalue_seen = {}
    for lvalue in left_list:
        try:
            lvalue_seen[lvalue] += 1
        except KeyError:
            lvalue_seen[lvalue] = 1
            translation[lvalue] = 0

        if translation[lvalue] != 0:
            continue
        number_of_occurance = 0
        for rvalue in right_list:
            if lvalue == rvalue:
                number_of_occurance += 1
        translation[lvalue] = number_of_occurance


    sim_sum = 0
    for lvalue in lvalue_seen:
        sim_sum += lvalue * lvalue_seen[lvalue] * translation[lvalue]

    print("Part 2: ", sim_sum)

if __name__ == "__main__":
    main()
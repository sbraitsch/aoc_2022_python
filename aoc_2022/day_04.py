from util import file_to_lines


def find_overlapping(lines: list[str], full: bool) -> int:
    acc = 0
    for line in lines:
        split = line.split(",")
        first = map_to_range(split[0])
        second = map_to_range(split[1])
        overlap = range(max(first[0], second[0]), min(first[-1], second[-1]) + 1)
        if len(overlap) > 0:
            str_rep = f"{overlap[0]}-{overlap[-1]}"
            if not full or (str_rep == split[0] or str_rep == split[1]):
                acc += 1

    return acc


def map_to_range(str_rep: str) -> range:
    rng = str_rep.split("-")
    return range(int(rng[0]), int(rng[1]) + 1)


def solve_part_one(lines: list[str]) -> int:
    return find_overlapping(lines, True)


def solve_part_two(lines: list[str]) -> int:
    return find_overlapping(lines, False)


if __name__ == "__main__":
    txt = file_to_lines("day_04.txt")

    print(f"Part 1: {solve_part_one(txt)}")
    print(f"Part 2: {solve_part_two(txt)}")

from file_parser import file_to_lines


def get_value(c: str) -> int:
    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96


def solve_part_one(lines: list[str]) -> int:
    acc = 0
    for line in lines:
        first_comp = line[:len(line) // 2]
        second_comp = line[len(line) // 2:]
        for c in first_comp:
            if c in second_comp:
                acc += get_value(c)
                break
    return acc


def solve_part_two(lines: list[str]) -> int:
    chunks = [lines[i:i+3] for i in range(0, len(lines), 3)]
    acc = 0
    for chunk in chunks:
        for c in chunk[0]:
            if (c in chunk[1]) and (c in chunk[2]):
                acc += get_value(c)
                break
    return acc


if __name__ == "__main__":
    lines = file_to_lines("day_03.txt")
    print(f"Part 1: {solve_part_one(lines)}")
    print(f"Part 2: {solve_part_two(lines)}")

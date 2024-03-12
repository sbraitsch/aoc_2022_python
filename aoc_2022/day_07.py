from util import calculate_execution_time, file_to_lines, file_to_str


def parse_file_tree(lines: list[str]) -> dict:
    file_tree = dict()
    current_dir = []
    for line in lines:
        match line[2:4]:
            case "cd":
                if line[5:7] == "..":
                    current_dir.pop()
                else:
                    current_dir.append(line[5:])
                    dir = "".join(d for d in current_dir)
                    file_tree[dir] = 0
            case "ls":
                pass
            case _:
                match line[:3]:
                    case "dir":
                        pass
                    case _:
                        size = line.split(" ")[0]
                        dir = "".join(d for d in current_dir)
                        file_tree[dir] += int(size)
                        dir_cp = current_dir.copy()
                        while len(dir_cp) > 1:
                            dir_cp.pop()
                            parent = "".join(d for d in dir_cp)
                            file_tree[parent] += int(size)

    return file_tree


@calculate_execution_time
def solve_part_one(tree: dict) -> int:
    return sum(value for _, value in tree.items() if value <= 100000)


@calculate_execution_time
def solve_part_two(tree: dict) -> int:
    to_free = 30_000_000 - (70_000_000 - tree["/"])
    return min(value for _, value in tree.items() if value >= to_free)


if __name__ == "__main__":
    lines = file_to_lines("day_07.txt")
    file_tree = parse_file_tree(lines)

    print(f"Part 1: {solve_part_one(file_tree)}")
    print(f"Part 2: {solve_part_two(file_tree)}")

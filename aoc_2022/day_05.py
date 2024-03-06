from file_parser import file_to_lines


def move_crates(moves: list[list[int]], stacks: list[list[str]], mover9001: bool) -> str:
    for amount, fr, to in moves:
        crates = stacks[fr][-amount:]
        if not mover9001:
            crates.reverse()
        stacks[fr] = stacks[fr][:-amount]
        stacks[to].extend(crates)

    return ''.join([stack[-1] for stack in stacks])


def solve_part_one(moves: list[list[int]], stacks: list[list[str]]) -> str:
    return move_crates(moves, stacks, False)


def solve_part_two(moves: list[list[int]], stacks: list[list[str]]) -> str:
    return move_crates(moves, stacks, True)


if __name__ == "__main__":
    txt = file_to_lines("day_05.txt")
    stacks = [[] for _ in range(9)]
    port = txt[:9]
    port.reverse()
    moves = txt[10::]
    for row in port:
        for i, c in enumerate(row):
            if c.isalpha():
                stacks[i // 4].append(c)

    parsed_moves = []
    for move in moves:
        split = move.split(' ')
        parsed_moves.append([int(split[1]), int(split[3]) - 1, int(split[5]) - 1])

    print(f"Part 1: {solve_part_one(parsed_moves, stacks.copy())}")
    print(f"Part 2: {solve_part_two(parsed_moves, stacks)}")

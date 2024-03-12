from util import calculate_execution_time, file_to_lines, file_to_str


def tree_visible(trees: list[str], x: int, y: int) -> tuple:
    height = int(trees[y][x])
    blocked = 0
    cur_view = 0
    view = 0

    for pos in range(y - 1, -1, -1):
        tree_at = trees[pos][x]
        cur_view = y - pos
        if int(tree_at) >= height:
            blocked += 1
            break

    view += cur_view

    for pos in range(x + 1, 99):
        tree_at = trees[y][pos]
        cur_view = pos - x
        if int(tree_at) >= height:
            blocked += 1
            break

    view *= cur_view

    for pos in range(y + 1, 99):
        tree_at = trees[pos][x]
        cur_view = pos - y
        if int(tree_at) >= height:
            blocked += 1
            break

    view *= cur_view

    for pos in range(x - 1, -1, -1):
        tree_at = trees[y][pos]
        cur_view = x - pos
        if int(tree_at) >= height:
            blocked += 1
            break

    view *= cur_view

    return (blocked != 4, view)


@calculate_execution_time
def solve_both(trees: list[str]) -> tuple:
    visible = 0
    max_view = 0
    for y in range(1, 98):
        for x in range(1, 98):
            vis, view = tree_visible(trees, x, y)
            if vis:
                visible += 1
            max_view = max(max_view, view)
    return (visible + (2 * 99) + (2 * 97), max_view)


if __name__ == "__main__":
    lines = file_to_lines("day_08.txt")

    print(f"Part 1+2: {solve_both(lines)}")

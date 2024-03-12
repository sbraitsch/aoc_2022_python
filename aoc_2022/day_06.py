from util import calculate_execution_time, file_to_str
from collections import deque


def check_marker_unique(marker: str) -> bool:
    seen = set()
    for c in marker:
        if c in seen:
            return False
        else:
            seen.add(c)
    return True


def find_marker(datastream: str, marker_len: int) -> int:
    marker = deque([], marker_len)
    for i, c in enumerate(datastream):
        marker.appendleft(c)
        if len(marker) == marker_len and check_marker_unique("".join(marker)):
            return i + 1
    return 0


@calculate_execution_time
def solve_part_one(datastream: str) -> int:
    return find_marker(datastream, 4)


@calculate_execution_time
def solve_part_two(datastream: str) -> int:
    return find_marker(datastream, 14)


if __name__ == "__main__":
    txt = file_to_str("day_06.txt")

    print(f"Part 1: {solve_part_one(txt)}")
    print(f"Part 2: {solve_part_two(txt)}")

from file_parser import file_to_str
from _collections import deque


def check_marker_unique(marker: str) -> bool:
    num = 0
    for c in marker:
        num |= 1 << (ord(c) - ord('a'))
    return len(marker) == bin(num).count('1')


def find_marker(datastream: str, marker_len: int) -> int:
    marker = deque([], marker_len)
    for i, c in enumerate(datastream):
        marker.appendleft(c)
        if len(marker) == marker_len and check_marker_unique(''.join(marker)):
            return i + 1
    return 0


def solve_part_one(datastream: str) -> int:
    return find_marker(datastream, 4)


def solve_part_two(datastream:str) -> int:
    return find_marker(datastream, 14)


if __name__ == "__main__":
    txt = file_to_str("day_06.txt")

    print(f"Part 1: {solve_part_one(txt)}")
    print(f"Part 2: {solve_part_two(txt)}")

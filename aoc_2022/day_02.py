from util import file_to_lines


def solve_part_one(lines: list[str]) -> int:
    session_value = 0
    for line in lines:
        game_result = 0
        match line:
            case "A X" | "B Y" | "C Z":
                game_result = 3
            case "A Z" | "B X" | "C Y":
                game_result = 0
            case "A Y" | "B Z" | "C X":
                game_result = 6
        session_value += game_result + (ord(line[2]) - b"W"[0])
    return session_value


def solve_part_two(lines: list[str]) -> int:
    session_value = 0
    for line in lines:
        game_result = 0
        picks = []
        match line[2]:
            case "X":
                game_result = 0
                picks = [3, 1, 2]
            case "Y":
                game_result = 3
                picks = [1, 2, 3]
            case "Z":
                game_result = 6
                picks = [2, 3, 1]
        session_value += game_result + picks[ord(line[0]) - b"A"[0]]
    return session_value


if __name__ == "__main__":
    lines = file_to_lines("day_02.txt")
    print(f"Part 1: {solve_part_one(lines)}")
    print(f"Part 2: {solve_part_two(lines)}")

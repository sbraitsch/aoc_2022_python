from file_parser import file_to_lines
import heapq

def build_heap(lines: list[str]):
    heap = []
    cur_cal = 0
    for line in lines:
        if line != '\n':
            cur_cal += int(line)
        else:
            heapq.heappush(heap, cur_cal)
            cur_cal = 0
    
    return heap

def solve_part_one(heap):
    return heapq.nlargest(1, heap)


def solve_part_two(heap):
    return sum(heapq.nlargest(3, heap), 0)


if __name__ == "__main__":
    lines: list[str] = file_to_lines('day_01.txt')
    heap = build_heap(lines)
    print(solve_part_one(heap))
    print(solve_part_two(heap))

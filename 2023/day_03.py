from collections import defaultdict
from functools import reduce
from operator import mul
import re

with open("input.txt", "r", encoding="utf8") as file:
    data_input = file.readlines()
data = [x.strip() for x in data_input]


def part1(data):
    # solves part1 problem and prepares data for part2
    number_regex = re.compile(r"(\d+)")

    total_sum = 0
    graph = defaultdict(list)

    for current_row, line in enumerate(data):
        for match in number_regex.finditer(line):
            num = int(match.group(1))
            add_to_sum = False

            start_row = max(current_row - 1, 0)
            end_row = min(current_row + 1, len(data) - 1)
            start_pos = max(0, match.start(1) - 1)
            end_pos = min(match.end(1), len(line) - 1)

            for row in range(start_row, end_row + 1):
                for pos in range(start_pos, end_pos + 1):
                    char = data[row][pos]
                    if char != "." and not char.isdigit():
                        add_to_sum = True
                        if char == "*":
                            graph[(row, pos)].append(num)

            if add_to_sum:
                total_sum += num

    return total_sum, graph


def part2(graph):
    # solves part2 problem
    return sum([reduce(mul, x) for x in graph.values() if len(x) == 2])


part1_solution, part2_data = part1(data)
print(f"The solution for part 1 is {part1_solution} and part 2 is {part2(part2_data)}")

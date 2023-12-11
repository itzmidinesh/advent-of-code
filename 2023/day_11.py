import timeit, sys


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: Input file {file_path} not found.")
        sys.exit(1)


def calculate_distance(a, b, width, height, expansion):
    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])

    for x in width:
        if a[0] < x < b[0] or b[0] < x < a[0]:
            distance += expansion

    for y in height:
        if a[1] < y < b[1] or b[1] < y < a[1]:
            distance += expansion

    return distance


def solve_data(data, expansion):
    width = len(data[0])
    height = len(data)

    galaxy = [
        (j, i) for i, line in enumerate(data) for j, c in enumerate(line) if c == "#"
    ]

    gx = {x for x, _ in galaxy}
    gy = {y for _, y in galaxy}

    width = set(range(width)) - gx
    height = set(range(height)) - gy

    distance = 0
    for i, point1 in enumerate(galaxy):
        for point2 in galaxy[i + 1 :]:
            distance += calculate_distance(point1, point2, width, height, expansion)
    return distance


def part1(data):
    # solves part1 problem
    # expansion is passed as 1 to make each empty row/column twice as big.
    return solve_data(data, 1)


def part2(data):
    # solves part2 problem
    # expansion is passed as 999999 to make each empty row/column one million times larger.
    return solve_data(data, 999999)


def measure_time(func, args):
    return timeit.timeit(
        stmt=f"{func}({args})", setup=f"from __main__ import {func}, {args}", number=1
    )


if __name__ == "__main__":
    data = read_data("input.txt")
    result_part1 = part1(data)
    result_part2 = part2(data)
    print(f"The solution for part 1 is {result_part1} and part 2 is {result_part2}")

    time_part1 = measure_time("part1", "data")
    time_part2 = measure_time("part2", "data")

    print(f"Time taken to execute part 1: {time_part1:.6f} seconds")
    print(f"Time taken to execute part 2: {time_part2:.6f} seconds")

import timeit, sys


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            data_input = file.readlines()
        return [x.strip() for x in data_input]
    except FileNotFoundError:
        print(f"Error: Input file {file_path} not found.")
        sys.exit(1)


def part1(data):
    # solves part1 problem
    visited = [[0] * WIDTH for _ in range(HEIGHT)]  # part 2
    start_x, start_y = -1, -1
    for index in range(HEIGHT):
        if "S" in data[index]:
            start_x = index
            start_y = data[index].find("S")

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    happy_symbols = ["-7J", "|LJ", "-FL", "|F7"]
    valid_start_directions = []
    for index in range(4):
        position = directions[index]
        next_x = start_x + position[0]
        next_y = start_y + position[1]
        if (
            next_x >= 0
            and next_x <= HEIGHT
            and next_y >= 0
            and next_y <= WIDTH
            and data[next_x][next_y] in happy_symbols[index]
        ):
            valid_start_directions.append(index)
    is_valid_start = 3 in valid_start_directions  # part 2
    transformations = {
        (0, "-"): 0,
        (0, "7"): 1,
        (0, "J"): 3,
        (2, "-"): 2,
        (2, "F"): 1,
        (2, "L"): 3,
        (1, "|"): 1,
        (1, "L"): 0,
        (1, "J"): 2,
        (3, "|"): 3,
        (3, "F"): 0,
        (3, "7"): 2,
    }
    current_direction = valid_start_directions[0]
    current_x = start_x + directions[current_direction][0]
    current_y = start_y + directions[current_direction][1]
    length = 1
    visited[start_x][start_y] = 1  # Part 2
    while (current_x, current_y) != (start_x, start_y):
        visited[current_x][current_y] = 1  # Part 2
        length += 1
        current_direction = transformations[
            (current_direction, data[current_x][current_y])
        ]
        current_x = current_x + directions[current_direction][0]
        current_y = current_y + directions[current_direction][1]
    return length // 2, is_valid_start, visited


def part2(data, is_valid_start, visited):
    # solves part2 problem
    count_tiles = 0
    for index in range(HEIGHT):
        inside = False
        for j in range(WIDTH):
            if visited[index][j]:
                if data[index][j] in "|JL" or (
                    data[index][j] == "S" and is_valid_start
                ):
                    inside = not inside
            else:
                count_tiles += inside
    return count_tiles


def measure_time(func, args):
    return timeit.timeit(
        stmt=f"{func}({args})", setup=f"from __main__ import {func}, {args}", number=1
    )


if __name__ == "__main__":
    data = read_data("input.txt")
    HEIGHT = len(data)
    WIDTH = len(data[0])

    result_part1, is_valid_start, visited = part1(data)
    result_part2 = part2(data, is_valid_start, visited)
    print(f"The solution for part 1 is {result_part1} and part 2 is {result_part2}")

    time_part1 = measure_time("part1", "data")
    time_part2 = measure_time("part2", "data, is_valid_start, visited")

    print(f"Time taken to execute part 1: {time_part1:.6f} seconds")
    print(f"Time taken to execute part 2: {time_part2:.6f} seconds")

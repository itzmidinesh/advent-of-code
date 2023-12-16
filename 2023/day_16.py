import time
from collections import defaultdict


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            return file.read().splitlines()

    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Input file {file_path} not found.")


def energized_count(beam, energized, coordinates, direction):
    while (
        coordinates[0] >= 0
        and coordinates[0] < len(beam[0])
        and coordinates[1] >= 0
        and coordinates[1] < len(beam)
        and direction not in energized[coordinates]
    ):
        energized[coordinates].append(direction)
        if beam[coordinates[1]][coordinates[0]] == "/":
            direction = (-direction[1], -direction[0])
        elif beam[coordinates[1]][coordinates[0]] == "\\":
            direction = (direction[1], direction[0])
        elif beam[coordinates[1]][coordinates[0]] == "-":
            if direction == (0, 1) or direction == (0, -1):
                energized_count(
                    beam, energized, (coordinates[0] + 1, coordinates[1]), (1, 0)
                )
                direction = (-1, 0)
        elif beam[coordinates[1]][coordinates[0]] == "|":
            if direction == (1, 0) or direction == (-1, 0):
                energized_count(
                    beam, energized, (coordinates[0], coordinates[1] + 1), (0, 1)
                )
                direction = (0, -1)
        coordinates = (coordinates[0] + direction[0], coordinates[1] + direction[1])
    return len(energized)


def part1(data):
    # solves part1 problem
    return energized_count(data, defaultdict(list), (0, 0), (1, 0))


def part2(data):
    # solves part2 problem
    width, height = len(data[0]), len(data)
    beam_starts = (
        [((x, 0), (0, 1)) for x in range(width)]
        + [((0, y), (1, 0)) for y in range(height)]
        + [((x, height - 1), (0, -1)) for x in range(width)]
        + [((width - 1, y), (-1, 0)) for y in range(height)]
    )

    return max(
        energized_count(data, defaultdict(list), coord, direction)
        for coord, direction in beam_starts
    )


if __name__ == "__main__":
    data = read_data("input.txt")
    # Measure time for part1
    start_time = time.time()
    result_part1 = part1(data)
    end_time = time.time()
    time_part1 = end_time - start_time

    # Measure time for part2
    start_time = time.time()
    result_part2 = part2(data)
    end_time = time.time()
    time_part2 = end_time - start_time

    print(f"The solution for part 1 is {result_part1} and part 2 is {result_part2}")
    print(f"Time taken to execute part 1: {time_part1:.6f} seconds")
    print(f"Time taken to execute part 2: {time_part2:.6f} seconds")

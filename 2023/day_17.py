import time
from heapq import heappop, heappush


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            return [[int(city_block) for city_block in line.strip()] for line in file]
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Input file {file_path} not found.")


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def in_bounds(position, grid):
    # check if position is within bounds
    return position[0] in range(len(grid)) and position[1] in range(len(grid[0]))


def find_min_heat_loss(grid, min_distance, max_distance):
    # return the minimum heat loss value using Dijkstra's algorithm
    q = [(0, 0, 0, -1)]
    visited = set()
    values = {}
    destination = (len(grid) - 1, len(grid[0]) - 1)
    while q:
        value, x, y, invalid = heappop(q)
        if (x, y) == destination:
            return value
        if (x, y, invalid) in visited:
            continue
        visited.add((x, y, invalid))
        for direction in range(4):
            increased_value = 0
            if direction == invalid or (direction + 2) % 4 == invalid:
                continue
            for distance in range(1, max_distance + 1):
                current_x = x + DIRS[direction][0] * distance
                current_y = y + DIRS[direction][1] * distance
                if current_x in range(len(grid)) and current_y in range(len(grid[0])):
                    increased_value += grid[current_x][current_y]
                    if distance < min_distance:
                        continue
                    new_value = value + increased_value
                    if (
                        values.get((current_x, current_y, direction), 1e100)
                        <= new_value
                    ):
                        continue
                    values[(current_x, current_y, direction)] = new_value
                    heappush(q, (new_value, current_x, current_y, direction))


if __name__ == "__main__":
    grid = read_data("input.txt")
    # Measure time for part1
    start_time = time.time()
    result_part1 = find_min_heat_loss(grid, 1, 3)
    end_time = time.time()
    time_part1 = end_time - start_time

    # Measure time for part2
    start_time = time.time()
    result_part2 = find_min_heat_loss(grid, 4, 10)
    end_time = time.time()
    time_part2 = end_time - start_time

    print(f"The solution for part 1 is {result_part1} and part 2 is {result_part2}")
    print(f"Time taken to execute part 1: {time_part1:.6f} seconds")
    print(f"Time taken to execute part 2: {time_part2:.6f} seconds")

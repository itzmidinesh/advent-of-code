from collections import deque
import time


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            return [list(row) for row in file.read().strip().split("\n")]
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Input file {file_path} not found.")


def find_distances(grid, start_row, start_column):
    distances = {}
    queue = deque([(0, 0, start_row, start_column, 0)])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while queue:
        total_row, total_col, row, col, distance = queue.popleft()
        if row < 0:
            total_row -= 1
            row += rows
        if row >= rows:
            total_row += 1
            row -= rows
        if col < 0:
            total_col -= 1
            col += cols
        if col >= cols:
            total_col += 1
            col -= cols
        if not (0 <= row < rows and 0 <= col < cols and grid[row][col] != "#"):
            continue
        if (total_row, total_col, row, col) in distances:
            continue
        if abs(total_row) > 4 or abs(total_col) > 4:
            continue
        distances[(total_row, total_col, row, col)] = distance
        for d_row, d_col in directions:
            queue.append((total_row, total_col, row + d_row, col + d_col, distance + 1))
    return distances


def solve(distance, value, total_steps, solved_cache):
    amount = (total_steps - distance) // rows
    if (distance, value, total_steps) in solved_cache:
        return solved_cache[(distance, value, total_steps)]
    result = 0
    for x in range(1, amount + 1):
        if distance + rows * x <= total_steps and (distance + rows * x) % 2 == (
            total_steps % 2
        ):
            result += (x + 1) if value == 2 else 1
    solved_cache[(distance, value, total_steps)] = result
    return result


def solve23(distances, part):
    total_steps = 64 if part == 1 else 26501365
    answer = 0
    solved_cache = {}
    options = [x for x in range(-3, 4)]
    options_range = [min(options), max(options)]
    for row_index in range(rows):
        for col_index in range(cols):
            if (0, 0, row_index, col_index) in distances:
                for total_row in options:
                    for total_col in options:
                        if part == 1 and (total_row != 0 or total_col != 0):
                            continue
                        distance = distances[
                            (total_row, total_col, row_index, col_index)
                        ]
                        if distance % 2 == total_steps % 2 and distance <= total_steps:
                            answer += 1
                        if total_row in options_range and total_col in options_range:
                            answer += solve(distance, 2, total_steps, solved_cache)
                        elif total_row in options_range or total_col in options_range:
                            answer += solve(distance, 1, total_steps, solved_cache)
    return answer


if __name__ == "__main__":
    grid = read_data("input.txt")
    rows, cols = len(grid), len(grid[0])
    start_row, start_column = next(
        (row, col)
        for row in range(rows)
        for col in range(cols)
        if grid[row][col] == "S"
    )
    distances = find_distances(grid, start_row, start_column)

    # Measure time for part1
    start_time = time.time()
    result_part1 = solve23(distances, 1)
    end_time = time.time()
    time_part1 = end_time - start_time
    print(f"Time taken to execute part 1: {time_part1:.6f} seconds")

    # Measure time for part2
    start_time = time.time()
    print("Running to solve Part 2, please wait...")
    result_part2 = solve23(distances, 2)
    end_time = time.time()
    time_part2 = end_time - start_time
    print(f"Time taken to execute part 2: {time_part2:.6f} seconds")
    print(f"The solution for part 1 is {result_part1} and part 2 is {result_part2}")

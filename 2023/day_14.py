import time


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            data_input = file.readlines()
        return [[char for char in line.strip()] for line in data_input]
    except FileNotFoundError:
        print(f"Error: Input file {file_path} not found.")


def roll(grid, row_count, col_count):
    for col in range(col_count):
        for _ in range(row_count):
            for row in range(row_count):
                if grid[row][col] == "O" and row > 0 and grid[row - 1][col] == ".":
                    grid[row][col] = "."
                    grid[row - 1][col] = "O"
    return grid


def score(grid, row_count, col_count):
    result = 0
    for row in range(row_count):
        for col in range(col_count):
            if grid[row][col] == "O":
                result += len(grid) - row
    return result


def rotate(grid, row_count, col_count):
    rotated_grid = [["?" for _ in range(row_count)] for _ in range(col_count)]
    for row in range(row_count):
        for col in range(col_count):
            rotated_grid[col][row_count - 1 - row] = grid[row][col]
    return rotated_grid


def part1(grid, row_count, col_count):
    # solves part1 problem
    return score(roll(grid, row_count, col_count), row_count, col_count)


def part2(grid, row_count, col_count):
    # solves part2 problem
    target = 10**9
    times = 0
    return score(find_cycle_length(grid, target, times), row_count, col_count)


def find_cycle_length(grid, target, times):
    stored_grid = {}
    while times < target:
        times += 1
        for _ in range(4):
            grid = rotate(roll(grid, row_count, col_count), row_count, col_count)
        Gh = tuple(tuple(row) for row in grid)
        if Gh in stored_grid:
            cycle_length = times - stored_grid[Gh]
            amount = (target - times) // cycle_length
            times += amount * cycle_length
        stored_grid[Gh] = times
    return grid


if __name__ == "__main__":
    grid = read_data("input.txt")
    row_count = len(grid)
    col_count = len(grid[0])
    # Measure time for part1
    start_time = time.time()
    result_part1 = part1(grid, row_count, col_count)
    end_time = time.time()
    time_part1 = end_time - start_time

    # Measure time for part2
    start_time = time.time()
    result_part2 = part2(grid, row_count, col_count)
    end_time = time.time()
    time_part2 = end_time - start_time

    print(f"The solution for part 1 is {result_part1} and part 2 is {result_part2}")
    print(f"Time taken to execute part 1: {time_part1:.6f} seconds")
    print(f"Time taken to execute part 2: {time_part2:.6f} seconds")

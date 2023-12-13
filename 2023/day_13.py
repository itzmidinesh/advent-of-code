import timeit, sys


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            return file.read().split("\n\n")
    except FileNotFoundError:
        print(f"Error: Input file {file_path} not found.")
        sys.exit(1)


def summarize(data, part2):
    # solves part1/part2 based on the part2 parameter(boolean)
    summary = 0
    for pattern in data:
        current_pattern = [[char for char in line] for line in pattern.split("\n")]
        rows, columns = len(current_pattern), len(current_pattern[0])

        # check vertical symmetry
        for prev_col in range(columns - 1):
            smudge = 0
            for col in range(columns):
                left_col, right_col = prev_col - col, prev_col + col + 1
                if 0 <= left_col < right_col < columns:
                    for row in range(rows):
                        if (
                            current_pattern[row][left_col]
                            != current_pattern[row][right_col]
                        ):
                            smudge += 1
            if smudge == (1 if part2 else 0):
                summary += prev_col + 1

        # check horizontal symmetry
        for prev_row in range(rows - 1):
            smudge = 0
            for row in range(rows):
                up_row, down_row = prev_row - row, prev_row + 1 + row
                if 0 <= up_row < down_row < rows:
                    for col in range(columns):
                        if (
                            current_pattern[up_row][col]
                            != current_pattern[down_row][col]
                        ):
                            smudge += 1
            if smudge == (1 if part2 else 0):
                summary += 100 * (prev_row + 1)
    return summary


def measure_time(func, args):
    return timeit.timeit(
        stmt=f"{func}({args})", setup=f"from __main__ import {func}, {args}", number=1
    )


if __name__ == "__main__":
    data = read_data("input.txt")
    result_part1 = summarize(data, False)
    result_part2 = summarize(data, True)
    print(f"The solution for part 1 is {result_part1} and part 2 is {result_part2}")
    for part in [False, True]:
        time_part = measure_time("summarize", "data, part")
        print(f"Time taken to execute part {part}: {time_part:.6f} seconds")

import timeit, sys


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            data_input = file.readlines()
        return [[int(number) for number in line.strip().split()] for line in data_input]
    except FileNotFoundError:
        print(f"Error: Input file {file_path} not found.")
        sys.exit(1)


def sum_sequence(line):
    # Base case for stopping recursion: if all elements in the line are 0, return 0
    if sum(number != 0 for number in line) == 0:
        return 0
    # Calculate the differences between consecutive numbers and put in a list
    sequence = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    # Recursively calculate the sum of last elements and return it
    return line[-1] + sum_sequence(sequence)


def part1(data):
    # solves part1 problem
    return sum(sum_sequence(line) for line in data)


def part2(data):
    # solves part2 problem
    return sum(sum_sequence(line[::-1]) for line in data)


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

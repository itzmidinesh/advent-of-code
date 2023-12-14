import time


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            data_input = file.readlines()
        return [x.strip() for x in data_input]
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Input file {file_path} not found.")


def part1(data):
    # solves part1 problem
    return 0


def part2(data):
    # solves part2 problem
    return 0


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

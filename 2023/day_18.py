import time


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            data_input = file.read().strip().split("\n")
        return [x for x in data_input]
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Input file {file_path} not found.")


DIR_INDEX = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIR = ["R", "D", "L", "U"]
BASE_16 = 16


def solve(data, part2):
    # returns area of the polygon by using shoelace formula
    hole_index = (0, 0)
    hole_indices = [hole_index]
    perimeter = 0
    for line in data:
        if part2:
            direction = DIR_INDEX[int(line[-2])]
            distance = int(line[-7:-2], 16)  # convert from hexadecimal to integer
        else:
            direction = DIR_INDEX[DIR.index(line.split(" ")[0])]
            distance = int(line.split(" ")[1])
        new_x = hole_index[0] + direction[0] * distance
        new_y = hole_index[1] + direction[1] * distance
        hole_index = (new_x, new_y)
        perimeter += distance
        hole_indices.append(hole_index)
    hole_indices.reverse()
    area = 0
    for i in range(len(hole_indices) - 1):
        area += (hole_indices[i][0] - hole_indices[i + 1][0]) * (
            hole_indices[i][1] + hole_indices[i + 1][1]
        )
    return perimeter // 2 + area // 2 + 1


if __name__ == "__main__":
    data = read_data("input.txt")
    # Measure time for part1
    start_time = time.time()
    result_part1 = solve(data, False)
    end_time = time.time()
    time_part1 = end_time - start_time

    # Measure time for part2
    start_time = time.time()
    result_part2 = solve(data, True)
    end_time = time.time()
    time_part2 = end_time - start_time

    print(f"The solution for part 1 is {result_part1} and part 2 is {result_part2}")
    print(f"Time taken to execute part 1: {time_part1:.6f} seconds")
    print(f"Time taken to execute part 2: {time_part2:.6f} seconds")

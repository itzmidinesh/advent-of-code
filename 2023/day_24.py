import time
from z3 import *


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            return file.read().strip().split("\n")
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Input file {file_path} not found.")


def calculate_intersection(points, i, j):
    x1, x2 = points[i][0], points[i][0] + points[i][3]
    y1, y2 = points[i][1], points[i][1] + points[i][4]
    x3, x4 = points[j][0], points[j][0] + points[j][3]
    y3, y4 = points[j][1], points[j][1] + points[j][4]
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator != 0:
        intersection_x = (
            (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
        ) / denominator
        intersection_y = (
            (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
        ) / denominator
        valid_a = (intersection_x > x1) == (x2 > x1)
        valid_b = (intersection_x > x3) == (x4 > x3)

        return (
            200000000000000 <= intersection_x <= 400000000000000
            and 200000000000000 <= intersection_y <= 400000000000000
            and valid_a
            and valid_b
        )


def part1(points, points_count):
    # solves part1 problem
    result = 0
    for i in range(points_count):
        for j in range(i + 1, points_count):
            if calculate_intersection(points, i, j):
                result += 1
    return result


def part2(points, points_count):
    # solves part2 problem using z3 solver
    x, y, z, vx, vy, vz = [Int(var) for var in ("x", "y", "z", "vx", "vy", "vz")]
    time_variables = [Int(f"T{i}") for i in range(points_count)]
    z3_solver = Solver()

    for i in range(points_count):
        z3_solver.add(
            x + time_variables[i] * vx - points[i][0] - time_variables[i] * points[i][3]
            == 0
        )
        z3_solver.add(
            y + time_variables[i] * vy - points[i][1] - time_variables[i] * points[i][4]
            == 0
        )
        z3_solver.add(
            z + time_variables[i] * vz - points[i][2] - time_variables[i] * points[i][5]
            == 0
        )

    if z3_solver.check() == sat:
        model = z3_solver.model()
        return model.eval(x + y + z)


if __name__ == "__main__":
    lines = read_data("input.txt")
    points = [tuple(map(int, line.replace("@", ", ").split(", "))) for line in lines]
    points_count = len(points)
    # Measure time for part1
    start_time = time.time()
    result_part1 = part1(points, points_count)
    end_time = time.time()
    time_part1 = end_time - start_time

    # Measure time for part2
    start_time = time.time()
    result_part2 = part2(points, points_count)
    end_time = time.time()
    time_part2 = end_time - start_time

    print(f"The solution for part 1 is {result_part1} and part 2 is {result_part2}")
    print(f"Time taken to execute part 1: {time_part1:.6f} seconds")
    print(f"Time taken to execute part 2: {time_part2:.6f} seconds")

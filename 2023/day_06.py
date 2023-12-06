import re, math, timeit
from functools import reduce

with open("input.txt", "r", encoding="utf8") as file:
    data_input = file.readlines()
data = [x.strip() for x in data_input]


def get_num_ways(time, dist):
    # calculate number of ways based on time and distance
    sqrt_discriminant = (time**2 - 4 * dist) ** 0.5
    root1 = (time - sqrt_discriminant) / 2
    root2 = (time + sqrt_discriminant) / 2
    start = math.ceil(root1) if not root1.is_integer() else int(root1 + 1)
    end = math.floor(root2) if not root2.is_integer() else int(root2 - 1)
    return end - start + 1


def part1(data):
    # solves part1 problem
    values = [
        list(map(int, re.findall(r"\d+", line.split(":")[1].strip()))) for line in data
    ]
    time, dist = values
    return reduce(
        lambda x, y: x * y,
        [get_num_ways(t, d) for t, d in zip(time, dist)],
    )


def part2(data):
    # solves part2 problem
    values = [int("".join(line.split(":")[1].split())) for line in data]
    time, dist = values
    return get_num_ways(time, dist)


print(f"The solution for part 1 is {part1(data)} and part 2 is {part2(data)}")


def measure_time(func, args):
    # Measure the execution time of a function using timeit
    return timeit.timeit(
        stmt=f"{func}({args})", setup=f"from __main__ import {func}, {args}", number=1
    )


if __name__ == "__main__":
    time_part1 = measure_time("part1", "data")
    time_part2 = measure_time("part2", "data")

    print(f"Time taken to execute part 1: {time_part1:.6f} seconds")
    print(f"Time taken to execute part 2: {time_part2:.6f} seconds")

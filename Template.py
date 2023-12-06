import timeit


def part1(data):
    # solves part1 problem
    return 0


def part2(data):
    # solves part2 problem
    return 0


with open("input.txt", "r", encoding="utf8") as file:
    data_input = file.readlines()
data = [x.strip() for x in data_input]

print(f"The solution for part 1 is {part1(data)} and part 2 is {part2(data)}")


# Measure the execution time using timeit
def measure_time(func, args):
    return timeit.timeit(
        stmt=f"{func}({args})", setup=f"from __main__ import {func}, {args}", number=1
    )


if __name__ == "__main__":
    time_part1 = measure_time("part1", "data")
    time_part2 = measure_time("part2", "data")

    print(f"Time taken to execute part 1: {time_part1:.6f} seconds")
    print(f"Time taken to execute part 2: {time_part2:.6f} seconds")

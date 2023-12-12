import timeit, sys


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            data_input = file.readlines()
        return [line.strip() for line in data_input]
    except FileNotFoundError:
        print(f"Error: Input file {file_path} not found.")
        sys.exit(1)


def sum_arrangement_count(data, part):
    total = 0
    for line in data:
        springs, criteria = line.split()
        if part == 2:
            springs = "?".join([springs] * 5)
            criteria = ",".join([criteria] * 5)
        criteria = [int(criterion) for criterion in criteria.split(",")]
        results = {}
        total += count_possible_arrangements(springs, criteria, 0, 0, 0, results)
    return total


def count_possible_arrangements(
    springs, criteria, spring_index, criteria_index, spring_block_length, results
):
    current_key = (spring_index, criteria_index, spring_block_length)
    if current_key in results:
        return results[current_key]
    if spring_index == len(springs):
        if criteria_index == len(criteria) and spring_block_length == 0:
            return 1
        elif (
            criteria_index == len(criteria) - 1
            and criteria[criteria_index] == spring_block_length
        ):
            return 1
        else:
            return 0
    count = 0
    for char in [".", "#"]:
        if springs[spring_index] == char or springs[spring_index] == "?":
            if char == "." and spring_block_length == 0:
                count += count_possible_arrangements(
                    springs, criteria, spring_index + 1, criteria_index, 0, results
                )
            elif (
                char == "."
                and spring_block_length > 0
                and criteria_index < len(criteria)
                and criteria[criteria_index] == spring_block_length
            ):
                count += count_possible_arrangements(
                    springs, criteria, spring_index + 1, criteria_index + 1, 0, results
                )
            elif char == "#":
                count += count_possible_arrangements(
                    springs,
                    criteria,
                    spring_index + 1,
                    criteria_index,
                    spring_block_length + 1,
                    results,
                )
    results[current_key] = count
    return count


def measure_time(func, args):
    return timeit.timeit(
        stmt=f"{func}({args})", setup=f"from __main__ import {func}, {args}", number=1
    )


if __name__ == "__main__":
    data = read_data("input.txt")
    result_part1 = sum_arrangement_count(data, 1)
    result_part2 = sum_arrangement_count(data, 2)
    print(f"The solution for part 1 is {result_part1} and part 2 is {result_part2}")
    for part in [1, 2]:
        time_part = measure_time("sum_arrangement_count", "data, part")
        print(f"Time taken to execute part {part}: {time_part:.6f} seconds")

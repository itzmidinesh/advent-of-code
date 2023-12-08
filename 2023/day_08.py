import timeit, sys, math


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            data_input = file.read().split("\n\n")
        return [x.strip() for x in data_input]
    except FileNotFoundError:
        print(f"Error: Input file {file_path} not found.")
        sys.exit(1)


def split_data(data):
    instructions = list(data[0])
    nodes = {}
    for node in data[1].split("\n"):
        name = node.split(" ")[0]
        left = node.split("(")[1].split(",")[0]
        right = node.split(" ")[3].split(")")[0]
        nodes[name] = (left, right)
    return instructions, nodes


def part1(instructions, nodes):
    # solves part1 problem
    current_position = "AAA"
    steps = 0
    while current_position != "ZZZ":
        direction = instructions[steps % len(instructions)]
        current_position = nodes[current_position][0 if direction == "L" else 1]
        steps += 1
    return steps


def part2(instructions, nodes):
    # solves part2 problem
    steps = 1
    for node in nodes:
        if node.endswith("A"):
            current_position = node
            node_step = 0
            while not current_position.endswith("Z"):
                direction = instructions[node_step % len(instructions)]
                current_position = nodes[current_position][0 if direction == "L" else 1]
                node_step += 1
            steps = math.lcm(steps, node_step)
    return steps


def measure_time(func, args):
    return timeit.timeit(
        stmt=f"{func}({args})", setup=f"from __main__ import {func}, {args}", number=1
    )


if __name__ == "__main__":
    data = read_data("input.txt")
    instructions, nodes = split_data(data)
    result_part1 = part1(instructions, nodes)
    result_part2 = part2(instructions, nodes)
    print(f"The solution for part 1 is {result_part1} and part 2 is {result_part2}")

    time_part1 = measure_time("part1", "instructions, nodes")
    time_part2 = measure_time("part2", "instructions, nodes")

    print(f"Time taken to execute part 1: {time_part1:.6f} seconds")
    print(f"Time taken to execute part 2: {time_part2:.6f} seconds")

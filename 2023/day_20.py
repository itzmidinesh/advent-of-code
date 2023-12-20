import time
from collections import defaultdict
from math import prod


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


def parse_data(data):
    conjunctions = defaultdict(dict)
    modules = dict()
    rx_value = None
    for line in data:
        label, destinations = line.split(" -> ")
        module_name, module_type = (
            (label[1:], label[0]) if label[0] in "%&" else (label, "")
        )
        modules[module_name] = module_type, destinations.split(", ")
        for destination in destinations.split(", "):
            conjunctions[destination][module_name] = 0
            rx_value = module_name if destination == "rx" else rx_value
    rx_dict = {i: 0 for i in conjunctions[rx_value]}
    return modules, conjunctions, rx_dict


def solve(data, part):
    curr_button_presses = 0
    button_presses = [0, 0]
    modules, conjunctions, rx_dict = parse_data(data)
    flip_flops = defaultdict(int)
    while True:
        if part == 1 and curr_button_presses == 1000:
            return prod(button_presses)
        if part == 2 and all(rx_dict.values()):
            return prod(rx_dict.values())
        curr_button_presses += 1
        queue = [(None, "broadcaster", 0)]
        while queue:
            source, module, pulse_input = queue.pop(0)
            button_presses[pulse_input] += 1
            if module not in modules:
                continue
            module_type, destinations = modules[module]
            if module_type == "":
                pulse_output = pulse_input
            elif module_type == "%" and pulse_input == 0:
                pulse_output = flip_flops[module] = not flip_flops[module]
            elif module_type == "&":
                conjunctions[module][source] = pulse_input
                pulse_output = not all(conjunctions[module].values())
                if "rx" in destinations:
                    rx_dict.update(
                        {
                            key: curr_button_presses
                            for key, value in conjunctions[module].items()
                            if value
                        }
                    )
            else:
                continue
            for destination in destinations:
                queue.append((module, destination, pulse_output))


if __name__ == "__main__":
    data = read_data("input.txt")
    # Measure time for part1
    start_time = time.time()
    result_part1 = solve(data, 1)
    end_time = time.time()
    time_part1 = end_time - start_time

    # Measure time for part2
    start_time = time.time()
    result_part2 = solve(data, 2)
    end_time = time.time()
    time_part2 = end_time - start_time

    print(f"The solution for part 1 is {result_part1} and part 2 is {result_part2}")
    print(f"Time taken to execute part 1: {time_part1:.6f} seconds")
    print(f"Time taken to execute part 2: {time_part2:.6f} seconds")

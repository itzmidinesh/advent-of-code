import time


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            return file.read().split(",")
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Input file {file_path} not found.")


def hash(step):
    # takes a string and returns a hash based on the ascii value of each char in string
    current_value = 0
    for char in step:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def part1(data):
    # solves part1 problem
    sum = 0
    for step in data:
        sum += hash(step)
    return sum


def part2(data):
    # solves part2 problem
    sum = 0
    lenses = [[] for i in range(256)]
    focal_length = [{} for i in range(256)]
    for step in data:
        label = step.split("=")[0].split("-")[0]
        hash_value = hash(label)
        if "-" in step:
            if label in lenses[hash_value]:
                lenses[hash_value].remove(label)
        if "=" in step:
            if label not in lenses[hash_value]:
                lenses[hash_value].append(label)
            focal_length[hash_value][label] = int(step.split("=")[1])
    for box_index, box in enumerate(lenses):
        for slot_index, lens in enumerate(box):
            sum += (box_index + 1) * (slot_index + 1) * focal_length[box_index][lens]
    return sum


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

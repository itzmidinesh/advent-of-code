import time


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            workflows, ratings = file.read().split("\n\n")
            return workflows, ratings
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Input file {file_path} not found.")


def parse_workflows(workflows):
    # parses workflow into a dictionary
    # "name": ([(rule1, rule2,...)], last_rule)
    workflows_dict = {}
    for workflow in workflows.splitlines():
        name, rest = workflow[:-1].split("{")
        rules = rest.split(",")
        workflows_dict[name] = ([], rules.pop(-1))
        for rule in rules:
            test, destination = rule.split(":")
            workflows_dict[name][0].append((test, destination))
    return workflows_dict


def is_rating_accepted(workflows, ratings_dict, curr_workflow="in"):
    if curr_workflow == "R":
        return False
    if curr_workflow == "A":
        return True
    rules, fallback = workflows[curr_workflow]
    for rule in rules:
        condition = f"{rule[0][0]}={ratings_dict[rule[0][0]]}"
        exec(condition)
        if eval(rule[0]):
            return is_rating_accepted(workflows, ratings_dict, rule[1])
    return is_rating_accepted(workflows, ratings_dict, fallback)


def part1(workflows, ratings):
    total = 0
    for rating in ratings.splitlines():
        ratings_dict = {}
        parts = rating[1:-1].split(",")
        for part in parts:
            part_name, part_value = part.split("=")
            ratings_dict[part_name] = int(part_value)
        if is_rating_accepted(workflows, ratings_dict):
            total += sum(ratings_dict.values())
    return total


def part2(range, workflows, curr_workflow="in"):
    if curr_workflow == "R":
        return False
    if curr_workflow == "A":
        product = 1
        for min_range, max_range in range.values():
            product *= max_range - min_range + 1
        return product
    rules, fallback = workflows[curr_workflow]
    total = 0
    for rule, target in rules:
        min_range, max_range = range[rule[0]]
        rating_value = int(rule[2:])
        if rule[1] == "<":
            valid_range = (min_range, rating_value - 1)
            invalid_range = (rating_value, max_range)
        else:
            valid_range = (rating_value + 1, max_range)
            invalid_range = (min_range, rating_value)
        if valid_range[0] <= valid_range[1]:
            new_range = dict(range)
            new_range[rule[0]] = valid_range
            total += part2(new_range, workflows, target)
        if invalid_range[0] <= invalid_range[1]:
            range = dict(range)
            range[rule[0]] = invalid_range
        else:
            break
    else:
        total += part2(range, workflows, fallback)
    return total


if __name__ == "__main__":
    workflows, ratings = read_data("test.txt")
    parsed_workflows = parse_workflows(workflows)

    # Measure time for part1
    start_time = time.time()
    result_part1 = part1(parsed_workflows, ratings)
    end_time = time.time()
    time_part1 = end_time - start_time

    # Measure time for part2
    start_time = time.time()
    result_part2 = part2({key: (1, 4000) for key in "xmas"}, parsed_workflows)
    end_time = time.time()
    time_part2 = end_time - start_time

    print(f"The solution for part 1 is {result_part1} and part 2 is {result_part2}")
    print(f"Time taken to execute part 1: {time_part1:.6f} seconds")
    print(f"Time taken to execute part 2: {time_part2:.6f} seconds")

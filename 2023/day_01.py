with open("input.txt", "r", encoding="utf8") as file:
    data_input = file.readlines()
data = [x.strip() for x in data_input]


def part1(data):
    # solves part1 problem
    result = 0
    for line in data:
        line_result = ""
        for char in line:
            if char.isdigit():
                line_result += char
        result += int(f"{line_result[0]}{line_result[-1]}")
    return result


def part2(data):
    # solves part2 problem
    result = 0
    for line in data:
        line_result = ""
        for i, char in enumerate(line):
            if char.isdigit():
                line_result += char
            for d, val in enumerate(
                ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
            ):
                if line[i:].startswith(val):
                    line_result += str(d + 1)
        result += int(line_result[0] + line_result[-1])
    return result


print(f"The solution for part 1 is {part1(data)} and part 2 is {part2(data)}")

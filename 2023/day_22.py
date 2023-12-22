from collections import defaultdict
import sys, time

sys.setrecursionlimit(1000)


def read_data(file_path):
    """
    Read data from the input file and return a list of 2 tuples containing brick coordinates.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            return [
                [
                    tuple(int(a) for a in coords.split(","))
                    for coords in brick.strip().split("~")
                ]
                for brick in file
            ]
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Input file {file_path} not found.")


def is_intersection(l1, r1, l2, r2):
    return r1[0] >= l2[0] and l1[0] <= r2[0] and r1[1] >= l2[1] and l1[1] <= r2[1]


def part1(brick, bricks_up, bricks_down):
    for brick_above in bricks_up[brick]:
        if len(bricks_down[brick_above] - set([brick])) == 0:
            return False
    return True


def part2(brick, bricks_up, bricks_down, falling_bricks):
    if brick in falling_bricks:
        return
    else:
        falling_bricks.add(brick)
        for brick_above in bricks_up[brick]:
            if len(bricks_down[brick_above] - falling_bricks) == 0:
                part2(brick_above, bricks_up, bricks_down, falling_bricks)


def solve(data, part):
    # solves problem based on part received
    levels = defaultdict(list)
    bricks = []
    for _, (left, right) in enumerate(data):
        (current_left, current_right) = (left, right)
        while current_left[2] > 0:
            new_position = (
                (current_left[0], current_left[1], current_left[2] - 1),
                (current_right[0], current_right[1], current_right[2] - 1),
            )
            valid_position = True
            for position in levels[new_position[0][2]]:
                if is_intersection(
                    new_position[0],
                    new_position[1],
                    position[0],
                    position[1],
                ):
                    valid_position = False
                    break

            if not valid_position:
                break
            else:
                (current_left, current_right) = new_position

        for level in range(current_left[2], current_right[2] + 1):
            levels[level].append(
                (
                    (current_left[0], current_left[1], current_left[2]),
                    (current_right[0], current_right[1], current_right[2]),
                )
            )
        bricks.append((current_left, current_right))
    bricks_up = defaultdict(set)
    bricks_down = defaultdict(set)
    for brick in bricks:
        if brick[0][2] + 1 in levels:
            for candidates in levels[brick[0][2] - 1]:
                if is_intersection(brick[0], brick[1], candidates[0], candidates[1]):
                    bricks_up[candidates].add(brick)
                    bricks_down[brick].add(candidates)

    result = 0
    if part == 1:
        for brick in bricks:
            result += 1 if part1(brick, bricks_up, bricks_down) else 0

    if part == 2:
        for brick in bricks:
            falling_bricks = set()
            part2(brick, bricks_up, bricks_down, falling_bricks)
            result += len(falling_bricks) - 1
    return result


if __name__ == "__main__":
    data = read_data("input.txt")
    data.sort(key=lambda line: line[0][2])
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

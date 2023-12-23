import time


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


def part1(grid_data):
    # solves part1 problem
    adjacency_list = {}
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for row_idx, row in enumerate(grid_data):
        for col_idx, value in enumerate(row):
            if value == ".":
                for dr, dc in directions:
                    adj_row, adj_col = row_idx + dr, col_idx + dc
                    if not (0 <= adj_row < len(grid_data) and 0 <= adj_col < len(row)):
                        continue
                    if grid_data[adj_row][adj_col] == ".":
                        adjacency_list.setdefault((row_idx, col_idx), set()).add(
                            (adj_row, adj_col)
                        )
                        adjacency_list.setdefault((adj_row, adj_col), set()).add(
                            (row_idx, col_idx)
                        )
            if value == ">":
                adjacency_list.setdefault((row_idx, col_idx), set()).add(
                    (row_idx, col_idx + 1)
                )
                adjacency_list.setdefault((row_idx, col_idx - 1), set()).add(
                    (row_idx, col_idx)
                )
            if value == "v":
                adjacency_list.setdefault((row_idx, col_idx), set()).add(
                    (row_idx + 1, col_idx)
                )
                adjacency_list.setdefault((row_idx - 1, col_idx), set()).add(
                    (row_idx, col_idx)
                )
    rows, cols = len(grid_data), len(grid_data[0])
    queue = [(0, 1, 0)]
    visited_nodes = set()
    max_distance = 0
    while queue:
        current_row, current_col, distance = queue.pop()
        if distance == -1:
            visited_nodes.remove((current_row, current_col))
            continue
        if (current_row, current_col) == (rows - 1, cols - 2):
            max_distance = max(max_distance, distance)
            continue
        if (current_row, current_col) in visited_nodes:
            continue
        visited_nodes.add((current_row, current_col))
        queue.append((current_row, current_col, -1))
        for adj_row, adj_col in adjacency_list[(current_row, current_col)]:
            queue.append((adj_row, adj_col, distance + 1))

    return max_distance


def part2(grid_data):
    # solves part2 problem
    length_adjacency_list = {}  # (row, col) -> (adj_row, adj_col, length)
    for row_idx, row in enumerate(grid_data):
        for col_idx, value in enumerate(row):
            if value in ".>v":
                for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    adj_row, adj_col = row_idx + dr, col_idx + dc
                    if not (0 <= adj_row < len(grid_data) and 0 <= adj_col < len(row)):
                        continue
                    if grid_data[adj_row][adj_col] in ".>v":
                        length_adjacency_list.setdefault((row_idx, col_idx), set()).add(
                            (adj_row, adj_col, 1)
                        )
                        length_adjacency_list.setdefault((adj_row, adj_col), set()).add(
                            (row_idx, col_idx, 1)
                        )
    while True:
        for node, edges in length_adjacency_list.items():
            if len(edges) == 2:
                edge_a, edge_b = edges
                length_adjacency_list[edge_a[:2]].remove(node + (edge_a[2],))
                length_adjacency_list[edge_b[:2]].remove(node + (edge_b[2],))
                length_adjacency_list[edge_a[:2]].add(
                    (edge_b[0], edge_b[1], edge_a[2] + edge_b[2])
                )
                length_adjacency_list[edge_b[:2]].add(
                    (edge_a[0], edge_a[1], edge_a[2] + edge_b[2])
                )
                del length_adjacency_list[node]
                break
        else:
            break

    rows, cols = len(grid_data), len(grid_data[0])

    queue = [(0, 1, 0)]
    visited_nodes = set()
    max_distance = 0
    while queue:
        current_row, current_col, distance = queue.pop()
        if distance == -1:
            visited_nodes.remove((current_row, current_col))
            continue
        if (current_row, current_col) == (rows - 1, cols - 2):
            max_distance = max(max_distance, distance)
            continue
        if (current_row, current_col) in visited_nodes:
            continue
        visited_nodes.add((current_row, current_col))
        queue.append((current_row, current_col, -1))
        for adj_row, adj_col, length in length_adjacency_list[
            (current_row, current_col)
        ]:
            queue.append((adj_row, adj_col, distance + length))

    return max_distance


if __name__ == "__main__":
    grid_data = read_data("input.txt")
    print("Code Execution started, uses Brute force.\n")
    # Measure time for part1
    start_time = time.time()
    result_part1 = part1(grid_data)
    end_time = time.time()
    time_part1 = end_time - start_time
    print(f"Time taken to execute part 1: {time_part1:.6f} seconds")
    print(f"The solution for part 1 is {result_part1}\n")
    print("Part 2 is running. Please wait....")
    print("This might take some time based on the speed of your computer.")
    # Measure time for part2
    start_time = time.time()
    result_part2 = part2(grid_data)
    end_time = time.time()
    time_part2 = end_time - start_time
    print(f"Time taken to execute part 2: {time_part2:.6f} seconds")
    print(f"The solution for part 2 is {result_part2}")

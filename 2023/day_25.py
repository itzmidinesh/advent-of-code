from collections import defaultdict
import time
import networkx as nx


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            return [x.strip() for x in file.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Input file {file_path} not found.")


def part1(data):
    # solves part1 problem
    node_connections = defaultdict(set)
    for line in data:
        start, end = line.split(":")
        nodes = set(end.split())
        node_connections[start].update(nodes)
        for node in nodes:
            node_connections[node].add(start)
    graph = nx.DiGraph()
    for node, neighbors in node_connections.items():
        graph.add_edges_from(
            [(node, neighbor, {"capacity": 1.0}) for neighbor in neighbors]
        )
    source_node = next(iter(node_connections.keys()))
    for target_node in node_connections.keys() - {source_node}:
        cut_value, (left_set, right_set) = nx.minimum_cut(
            graph, source_node, target_node
        )
        if cut_value == 3:
            return len(left_set) * len(right_set)


if __name__ == "__main__":
    data = read_data("input.txt")
    # Measure time for part1
    start_time = time.time()
    result_part1 = part1(data)
    end_time = time.time()
    time_part1 = end_time - start_time

    print(f"The solution for part 1 is {result_part1}")
    print(f"Time taken to execute part 1: {time_part1:.6f} seconds\n")
    print(f"There is no part 2 for today's puzzle.")

import timeit, collections, sys


def read_data(file_path):
    """
    Read data from the input file and return a list of stripped lines.
    """
    try:
        with open(file_path, "r", encoding="utf8") as file:
            data_input = file.readlines()
        return [x.strip() for x in data_input]
    except FileNotFoundError:
        print(f"Error: Input file {file_path} not found.")
        sys.exit(1)


def solve_hand(hand, part):
    """
    Solve the hand and return a tuple with the maximum score and card indices.
    """
    CARDS = "J23456789TXQKA"
    HAND_TYPES = [
        (1, 1, 1, 1, 1),  # High card
        (1, 1, 1, 2),  # One pair
        (1, 2, 2),  # Two pairs
        (1, 1, 3),  # Three of a kind
        (2, 3),  # Full house
        (1, 4),  # Four of a kind
        (5,),  # Five of a kind
    ]
    if part == 1:
        hand = hand.replace("J", "X")
    card_index = [CARDS.index(card) for card in hand]
    total_score = [
        HAND_TYPES.index(
            tuple(sorted(collections.Counter(hand.replace("J", card)).values()))
        )
        for card in CARDS
    ]
    return (max(total_score), *card_index)


def calculate_results(data, part):
    """
    Calculate the final result based on the given part number.
    """
    result = sorted(
        (solve_hand(hand, part), int(bet))
        for hand, bet in (line.split() for line in data)
    )
    final_result = sum(index * bet + bet for index, (_, bet) in enumerate(result))
    return final_result


# Measure the execution time using timeit
if __name__ == "__main__":
    data = read_data("input.txt")

    result_part1 = calculate_results(data, 1)
    result_part2 = calculate_results(data, 2)

    print(f"The solution for part 1 is {result_part1} and part 2 is {result_part2}")

    setup_code = """
from __main__ import calculate_results, solve_hand, data
"""

    time_result1 = timeit.timeit(
        "calculate_results(data, 1)", setup=setup_code, number=1
    )
    time_result2 = timeit.timeit(
        "calculate_results(data, 2)", setup=setup_code, number=2
    )

    print(f"Time taken to execute part 1: {time_result1:.6f} seconds")
    print(f"Time taken to execute part 2: {time_result2:.6f} seconds")

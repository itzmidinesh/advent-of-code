import re
from collections import defaultdict

with open("input.txt", "r", encoding="utf8") as file:
    data_input = file.readlines()
data = [x.strip() for x in data_input]


def part1(data):
    # solves part1 problem
    total_points = 0
    regex_pattern = r"[:|]"
    for card in data:
        card_win_count = 0
        ticket = re.split(regex_pattern, card)
        winning_numbers = re.sub(r"\s+", " ", ticket[1].strip()).split(" ")
        holding_numbers = re.sub(r"\s+", " ", ticket[2].strip()).split(" ")
        card_win_count = sum(1 for i in holding_numbers if i in winning_numbers)
        total_points += (
            card_win_count if 0 <= card_win_count <= 2 else 2 ** (card_win_count - 1)
        )
    return total_points


def part2(data):
    # solves part2 problem
    ticket_count = defaultdict(lambda: 1)
    for card_index, card in enumerate(data):
        ticket = card.split(":")[1].split("|")
        ticket_count[card_index + 1]
        winning_numbers = set(map(int, ticket[0].split()))
        holding_numbers = set(map(int, ticket[1].split()))
        for n in range(len(winning_numbers.intersection(holding_numbers))):
            ticket_count[card_index + 2 + n] += ticket_count[card_index + 1]
    return sum(ticket_count.values())


print(f"The solution for part 1 is {part1(data)} and part 2 is {part2(data)}")

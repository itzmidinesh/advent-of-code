with open("input.txt", "r", encoding="utf8") as file:
    data_input = file.readlines()
data = [x.strip() for x in data_input]


def part1(data):
    # solves part1 problem
    red_max = 12
    green_max = 13
    blue_max = 14
    sum = 0
    for line in data:
        game = line.replace(":", ";").split(";")
        game_id = game[0].split(" ")[1]
        game_turn = [i.strip() for turn in game[1:] for i in turn.split(",")]
        count_possible = True
        for i in game_turn:
            single = i.split(" ")
            if (
                (single[1] == "red" and int(single[0]) > red_max)
                or (single[1] == "green" and int(single[0]) > green_max)
                or (single[1] == "blue" and int(single[0]) > blue_max)
            ):
                count_possible = False
        if count_possible == True:
            sum += int(game_id)
    return sum


def part2(data):
    # solves part2 problem
    sum = 0
    for line in data:
        product = 1
        game = line.replace(":", ";").split(";")
        game_turn = [i.strip() for turn in game[1:] for i in turn.split(",")]
        red_count = 0
        green_count = 0
        blue_count = 0
        for i in game_turn:
            single = i.split(" ")
            if single[1] == "red" and red_count < int(single[0]):
                red_count = int(single[0])
            elif single[1] == "green" and green_count < int(single[0]):
                green_count = int(single[0])
            elif single[1] == "blue" and blue_count < int(single[0]):
                blue_count = int(single[0])
        product *= red_count * green_count * blue_count
        sum += product
    return sum


print(f"The solution for part 1 is {part1(data)} and part 2 is {part2(data)}")

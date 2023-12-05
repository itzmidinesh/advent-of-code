with open("input.txt", "r", encoding="utf8") as file:
    seeds, *blocks = file.read().split("\n\n")

seeds = list(map(int, seeds.split(":")[1].split()))


def part1(seeds, blocks):
    # solves part1 problem
    for block in blocks:
        ranges = [list(map(int, line.split())) for line in block.splitlines()[1:]]
        updated_seeds = []

        for seed in seeds:
            for destination, source, length in ranges:
                if source <= seed < source + length:
                    updated_seeds.append(seed - source + destination)
                    break
            else:
                updated_seeds.append(seed)

        seeds = updated_seeds
    return min(seeds)


def part2(seeds, blocks):
    # solves part2 problem
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))

    for block in blocks:
        ranges = [list(map(int, line.split())) for line in block.splitlines()[1:]]
        updated_seeds = []
        while len(seed_ranges) > 0:
            start, end = seed_ranges.pop()
            for destination, source, length in ranges:
                overlap_start = max(start, source)
                overlap_end = min(end, source + length)
                if overlap_start < overlap_end:
                    updated_seeds.append(
                        (
                            overlap_start - source + destination,
                            overlap_end - source + destination,
                        )
                    )
                    if overlap_start > start:
                        seed_ranges.append((start, overlap_start))
                    if end > overlap_end:
                        seed_ranges.append((overlap_end, end))
                    break
            else:
                updated_seeds.append((start, end))
        seed_ranges = updated_seeds

    return min(seed_ranges)[0]


print(
    f"The solution for part 1 is {part1(seeds, blocks)} and part 2 is {part2(seeds, blocks)}"
)

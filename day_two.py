def parseInput():
    f = open("inputs/day2.txt", "r")
    games = [line.split(":")[1].split(";") for line in f]
    return games

def partOne(input):
    index, total = 1, 0
    maxes = {"red": 12, "green": 13, "blue": 14 }
    for game in input:
        is_valid = True
        for round in game:
            reds = int(round[(round.index("red")-3):round.index("red")-1]) if "red" in round else 0
            blues = int(round[(round.index("blue")-3):(round.index("blue")-1)]) if "blue" in round else 0
            greens = int(round[(round.index("green")-3):(round.index("green")-1)]) if "green" in round else 0
            if reds > maxes["red"] or blues > maxes["blue"] or greens > maxes["green"]:
                is_valid = False
                break
        if is_valid:
            total += index
        index += 1
    return total


def partTwo(input):
    total = 0
    for game in input:
        maxes = [0, 0, 0]
        for round in game:
            reds = int(round[(round.index("red")-3):round.index("red")-1]) if "red" in round else 0
            blues = int(round[(round.index("blue")-3):(round.index("blue")-1)]) if "blue" in round else 0
            greens = int(round[(round.index("green")-3):(round.index("green")-1)]) if "green" in round else 0
            maxes[0] = max(reds,maxes[0])
            maxes[1] = max(blues,maxes[1])
            maxes[2] = max(greens,maxes[2])

        total += maxes[0] * maxes[1] * maxes[2]
    return total

if __name__ == "__main__":
    input = parseInput()
    print("Part one:",partOne(input))
    print("Part two:",partTwo(input))
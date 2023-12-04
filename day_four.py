def parseInput():
    f = open("inputs/day4.txt","r")
    input = [line.split(":")[1].strip().split("|") for line in f.readlines()]
    f.close()
    return input


def partOne(input):
    score = 0
    for card in input:
        winners, ours = card[0].strip().split(" "), card[1].strip().split(" ")
        hits = [match for match in ours if match in winners and len(match) > 0]
        if len(hits) > 0:
            score += 2**(len(hits)-1)
    return score


def partTwo(input):
    index = 0
    copies = [1 for i in range(len(input))]
    for card in input:
        card_count = copies[index]
        winners, ours = card[0].strip().split(" "), card[1].strip().split(" ")
        hits = [match for match in ours if match in winners and len(match) > 0]
        if len(hits) > 0:
            for hit in range(1,len(hits)+1):
                copies[index+hit] += card_count
        index += 1
    return sum(copies)


if __name__ == "__main__":
    input = parseInput()
    print("part one:", partOne(input))
    print("part two:", partTwo(input))
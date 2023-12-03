def parseInput():
    f = open("inputs/day3.txt","r")
    input = f.read().split("\n")
    return input

def getNeighbors(left, right, j, width, depth):
    neighbors = []
    for col in range(left-1, right+1):
        for row in range(j-1,j+2):
            if row >= 0 and row < depth and col >= 0 and col < width and ( col < left or col == right or row < j or row > j):
                neighbors.append((row, col))
    return neighbors

def checkNeighbors(input, neighbors):
    for neighbor in neighbors:
        if input[neighbor[0]][neighbor[1]] != "." and not input[neighbor[0]][neighbor[1]].isnumeric():
            return True
    return False

def partOne(input):
    total, j = 0, 0
    for line in input:
        left, right = 0, 0
        while left < len(line):
            while left < len(line) and not line[left].isnumeric():
                left += 1
            right =  left
            while right < len(line) and line[right].isnumeric():
                right += 1
            if left < len(line):
                neighbors = getNeighbors(left, right, j, len(line), len(input))
                if checkNeighbors(input, neighbors):
                    total += int(line[left:right])
            left = right
        j += 1
    return total

def getNumber(input, row, col):
    left, right = col, col
    digit_positions = []
    while input[row][left].isnumeric() and left >= 0:
        left -= 1
    while right < len(input) and input[row][right].isnumeric():
        right += 1
    for i in range(left+1, right):
        digit_positions.append((row, i))
    return digit_positions

def isGear(input, star):
    neighbors, extract = [], []
    number_one, number_two = 0, 0
    for row in range(star[0]-1, star[0]+2):
        for col in range(star[1]-1, star[1]+2):
            if row != star[0] or col != star[1]:
                neighbors.append((row, col))

    for neighbor in neighbors:
        if input[neighbor[0]][neighbor[1]].isnumeric():
            extract = getNumber(input, neighbor[0], neighbor[1])

    neighbors = [neighbor for neighbor in neighbors if neighbor not in extract]

    if len(extract) > 0:
        number_one = int(input[extract[0][0]][extract[0][1]:extract[-1][1]+1])
        extract = []

    for neighbor in neighbors:
        if input[neighbor[0]][neighbor[1]].isnumeric():
            extract = getNumber(input, neighbor[0], neighbor[1])

    if len(extract) > 0:
        number_two = int(input[extract[0][0]][extract[0][1]:extract[-1][1]+1])

    if number_one > 0 and number_two > 0:
        return number_one * number_two
    else:
        return -1

def partTwo(input):
    stars = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "*":
                stars.append((i,j))
    values = [isGear(input, star) for star in stars if isGear(input, star) > 0]
    return sum(values)


if __name__ == "__main__":
    input = parseInput()
    print("part one:",partOne(input))
    print("part two:",partTwo(input))
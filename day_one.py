def parseInput():
    f = open("inputs/day1.txt", "r")
    lines = []
    for line in f:
        lines.append(line.strip())
    f.close()
    return lines

def partOne(input):
    sum = 0
    for line in input:
        digits = [c for c in line if '0' <= c <= '9']
        sum += (int(digits[0]) * 10) + int(digits[-1])
    return sum

def partTwo(input):
    replacements = {"one": "o1ne", "two": "t2wo", "three": "t3hree",
                    "four": "f4our", "five": "f5ive", "six": "s6ix",
                    "seven": "s7even", "eight": "e8ight", "nine": "n9ine"}
    parsed_digits = []
    for line in input:
        constructed_str = line
        for key, value in replacements.items():
            constructed_str = constructed_str.replace(key, value)
        parsed_digits.append(constructed_str)
    return partOne(parsed_digits)

def main():
    input = parseInput()
    print("Part One:", partOne(input))
    print("Part Two:", partTwo(input))

if __name__ == "__main__":
    main()

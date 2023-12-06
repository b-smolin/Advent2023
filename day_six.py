from functools import reduce

def parseInput():
    f = open("inputs/day6.txt")
    races = [race.split(":")[1].strip().split() for race in f.readlines()]
    f.close()
    return races

def parseTwo(times, records):
    time, record = "", ""
    for tme in times:
        time += tme
    for rcord in records:
        record += rcord
    return int(time), int(record)

def evalRace(time, record):
    count = 0
    for i in range(time):
        if ((time-i) * i) > record:
            #count += 1
            count = time - i - i + 1
            break

    return count

def partOne(times, records):
    results = [evalRace(int(times[i]), int(records[i])) for i in range(len(times))]
    print(results)
    return reduce((lambda x, y: x * y), results)
    
def partTwo(time, record):
    for i in range(time):
        if ((time-i) * i) > record:
            return time-(i*2)
        
if __name__ == "__main__":
    races = parseInput()
    times, records = races[0], races[1]
    time, record = parseTwo(times, records)
    print(partOne(times, records))
    print(evalRace(time,record))
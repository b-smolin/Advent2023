class range_struct:
    def __init__(self, destination, source, span) -> None:
        self.source = int(source)
        self.destination = int(destination)
        self.span = int(span)
    
    def __repr__(self) -> str:
        return str(self.source) + " " + str(self.destination) + " " + str(self.span)
    
    def getSource(self) -> tuple[int, int]:
        return (self.source, int(self.source) + (self.span))

    def getDestination(self) -> tuple[int, int]:
        return (self.destination, self.destination + self.span)
    
    def getLocation(self, seed: int) -> int:
        print(self)
        print(seed, seed- int(self.source), seed-int(self.source)+int(self.destination))
        return (seed - self.source + self.destination)

def parseInput():
    f = open("inputs/sample_day5.txt")
    raw = f.read().split("\n")
    f.close()
    seeds = [int(seed) for seed in raw[0].split()[1:]]
    index = raw.index("seed-to-soil map:")+1
    seed_to_soil = []
    while len(raw[index]) > 0:
        line = raw[index].split()
        seed_to_soil.append(range_struct(line[0],line[1],line[2]))
        index += 1
    index = raw.index("soil-to-fertilizer map:")+1
    soil_to_fertilizer = []
    while len(raw[index]) > 0:
        line = raw[index].split()
        soil_to_fertilizer.append(range_struct(line[0],line[1],line[2]))
        index += 1
    index = raw.index("fertilizer-to-water map:")+1
    fertilizer_to_water = []
    while len(raw[index]) > 0:
        line = raw[index].split()
        fertilizer_to_water.append(range_struct(line[0],line[1],line[2]))
        index += 1
    index = raw.index("water-to-light map:")+1
    water_to_light = []
    while len(raw[index]) > 0:
        line = raw[index].split()
        water_to_light.append(range_struct(line[0],line[1],line[2]))
        index += 1
    index = raw.index("light-to-temperature map:")+1
    light_to_temperature = []
    while len(raw[index]) > 0:
        line = raw[index].split()
        light_to_temperature.append(range_struct(line[0],line[1],line[2]))
        index += 1
    index = raw.index("temperature-to-humidity map:")+1
    temperature_to_humidity = []
    while len(raw[index]) > 0:
        line = raw[index].split()
        temperature_to_humidity.append(range_struct(line[0],line[1],line[2]))
        index += 1
    index = raw.index("humidity-to-location map:")+1
    humidity_to_location = []
    while index < len(raw) and len(raw[index]) > 0:
        line = raw[index].split()
        humidity_to_location.append(range_struct(line[0],line[1],line[2]))
        index += 1
    
    yield seeds
    yield seed_to_soil
    yield soil_to_fertilizer
    yield fertilizer_to_water
    yield water_to_light
    yield light_to_temperature
    yield temperature_to_humidity
    yield humidity_to_location

def partOne(seeds, mappings):
    print(seeds)
    for i in range(1,len(seeds)-1):
        for level in mappings:
            for rng in level: #range is dang keyword and i cant think of a better name
                if seeds[i] > int(rng.getSource()[0]) and seeds[i] < int(rng.getSource()[1]):
                    seeds[i] = rng.getLocation(seeds[i])
                    print(seeds)
                    break
                
    print(seeds)

    return min(seeds)

if __name__ == "__main__":
    inputs = [line for line in parseInput()]
    seeds = inputs[0]
    mappings = inputs[1:]
    print(partOne(seeds, mappings))
## Not my best work - ran brute force for 6 hrs for part 2 lmao
# A significantly faster input function
import sys

# Classes and functions here
def transform(n, d):
    # print(d)
    for x in d:
        if x[0] <= n <= x[0] + x[1]:
            diff = n - x[0]
            return d[x] + diff
    return n


def solve():
    n = sys.stdin.readlines()
    cats = [
        "seed-to-soil map:",
        "soil-to-fertilizer map:",
        "fertilizer-to-water map:",
        "water-to-light map:",
        "light-to-temperature map:",
        "temperature-to-humidity map:",
        "humidity-to-location map:",
    ]
    seed_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temp = {}
    temp_to_humidity = {}
    humiditiy_to_location = {}

    # parse through the data
    for i in range(len(n)):
        if n[i] == "\n":
            continue
        n[i] = n[i].strip()
        if i == 0:
            _, nums = n[i].split(":")
            nums = [int(x) for x in nums.split()]
        elif n[i] in cats:
            curr = n[i]
        elif n[i] != "":
            num = n[i].split()
            if curr == cats[0]:
                seed_to_soil[(int(num[1]), int(num[2]))] = int(num[0])
            elif curr == cats[1]:
                soil_to_fertilizer[(int(num[1]), int(num[2]))] = int(num[0])
            elif curr == cats[2]:
                fertilizer_to_water[(int(num[1]), int(num[2]))] = int(num[0])
            elif curr == cats[3]:
                water_to_light[(int(num[1]), int(num[2]))] = int(num[0])
            elif curr == cats[4]:
                light_to_temp[(int(num[1]), int(num[2]))] = int(num[0])
            elif curr == cats[5]:
                temp_to_humidity[(int(num[1]), int(num[2]))] = int(num[0])
            elif curr == cats[6]:
                humiditiy_to_location[(int(num[1]), int(num[2]))] = int(num[0])

    # print(nums)
    # print(seed_to_soil)
    # print(soil_to_fertilizer)
    # print(fertilizer_to_water)
    # print(water_to_light)
    # print(light_to_temp)
    # print(temp_to_humidity)
    # print(humiditiy_to_location)
    # ss = max(seed_to_soil)
    temp = []
    for i in range(0, len(nums), 2):
        temp.append(range(nums[i], nums[i] + nums[i + 1]))
    # # nums = [x for x in nums if x <= max_num]
    # nums = [x for x in nums if x <= ss]
    # nums.sort()
    msf = float("inf")
    for itr in temp:
        # print(n)
        # print("---------", n)
        for n in itr:
            # print(n)
            soil = transform(n, seed_to_soil)
            fertilizer = transform(soil, soil_to_fertilizer)
            water = transform(fertilizer, fertilizer_to_water)
            light = transform(water, water_to_light)
            temp = transform(light, light_to_temp)
            humiditiy = transform(temp, temp_to_humidity)
            location = transform(humiditiy, humiditiy_to_location)
            msf = min(location, msf)
            del soil, fertilizer, water, light, temp, humiditiy, location
    print("MSF")
    print(msf)


def main():
    for _ in range(1):
        solve()


if __name__ == "__main__":
    # Declare any global variables here
    main()

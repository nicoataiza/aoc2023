# A significantly faster input function
import sys

input = sys.stdin.readline

# Imports here

# Classes and functions here


def part1(nums):
    # nums = [0,3,6,9] ...
    out = nums[-1]
    diffs = []
    for i in range(len(nums)):
        if i == 0:
            continue
        diffs.append(nums[i] - nums[i - 1])
    while sum(diffs) != 0:
        out += diffs[-1]
        temp = []
        for i in range(len(diffs)):
            if i == 0:
                continue
            temp.append(diffs[i] - diffs[i - 1])
        diffs = temp
    out += diffs[-1]
    return out


def recur(nums, diffs):
    if sum(nums) == 0:
        return 0
    t = []
    for i in range(len(diffs)):
        if i == 0:
            continue
        t.append(diffs[i] - diffs[i - 1])
    return nums[0] - recur(diffs, t)


def part2(nums):
    out = nums[0]
    diffs = []
    for i in range(len(nums)):
        if i == 0:
            continue
        diffs.append(nums[i] - nums[i - 1])
    return recur(nums, diffs)


def solve():
    n = sys.stdin.readlines()
    n = [[int(i) for i in x.strip().split()] for x in n]
    t = []
    for nums in n:
        t.append(part2(nums))
    print(t)
    print(sum(t))


def main():
    # Change 'int(input())' to '1' if question only gives 1 test case
    for _ in range(1):
        solve()


if __name__ == "__main__":
    # Declare any global variables here
    main()

# A significantly faster input function
import sys

# Imports here


# Classes and functions here
def rename(n):
    nums = {
        "seven": "7",
        "eight": "8",
        "three": "3",
        "one": "1",
        "two": "2",
        "four": "4",
        "five": "5",
        "six": "6",
        "nine": "9",
    }
    l = 0
    r = 0
    temp = ""
    while True:
        if l >= len(n) - 1 or r > len(n):
            break

        for num in nums:
            if num in n[l:r]:
                print(num)
                temp += nums[num]
                l = r - 1
                r = l
                break
        if n[l].isnumeric():
            temp += n[l]
            l += 1
        try:
            if n[r].isnumeric():
                temp += n[r]
                l = r + 1
                r = l
        except:
            return temp
        r += 1
    return temp


def solve():
    file = r"/Users/nic/Downloads/input.txt"

    with open(file) as n:
        out = 0
        for x in n:
            x = rename(x)
            g = 0
            for y in x:
                if y.isnumeric():
                    g += 10 * int(y)
                    break
            for y in x[::-1]:
                if y.isnumeric():
                    g += int(y)
                    break
            out += g
        print(out)


def main():
    for _ in range(1):
        solve()


if __name__ == "__main__":
    # Declare any global variables here
    main()

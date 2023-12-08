# Had to yoink code to apply the LCM modules to iterables
# Intuition for part 2: Get each individual path and get the LCM of all nums
# A significantly faster input function
import sys
import math
import functools

input = sys.stdin.readline

# Imports here

# Classes and functions here


def get_moves(curr, d, moves):
    out = 0
    while curr[-1] != "Z":
        # print(curr)
        move = moves[out]
        if move == "R":
            curr = d[curr][1]
        else:
            curr = d[curr][0]
        if out >= len(moves) - 1:
            moves += moves
        out += 1
    return out


def solve():
    moves = input()
    moves = [x for x in moves.strip()]
    input()
    n = sys.stdin.readlines()
    d = {}
    out = 0
    curr = []
    # make adjacency list
    for node in n:
        source, dest = node.strip().split("=")
        source = source.strip()
        dest = dest.split(",")
        dest[0], dest[1] = dest[0].strip()[1:], dest[1].strip()[:-1]
        d[source] = dest
        if source[-1] == "A":
            curr.append(source)
    t = moves
    needed = []
    for x in curr:
        needed.append(get_moves(x, d, moves))
    print(functools.reduce(math.lcm, needed))


def main():
    # Change 'int(input())' to '1' if question only gives 1 test case
    for _ in range(1):
        solve()


if __name__ == "__main__":
    # Declare any global variables here
    main()

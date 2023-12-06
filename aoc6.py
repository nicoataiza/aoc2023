# He can't keep getting away with Brute-Force :') 
# A significantly faster input function
import sys
input = sys.stdin.readline

# Classes and functions here


def solve():
    out = 1
    t = input().split(':')
    d = input().split(':')

    times = t[1].strip().split()
    dist = d[1].strip().split()
    
    times = [int(x) for x in times]
    dist = [int(x) for x in dist]

    temp_t = [int(''.join([str(x) for x in times]))]
    dist_t = [int(''.join([str(x) for x in dist]))]

    times = temp_t
    dist = dist_t
    for i in range(len(times)):
        curr = 0 
        print(times[i],dist[i])
        for y in range(times[i] + 1):
            d_c = (y * (times[i] - y))
            if d_c > dist[i]:
                print(d_c)
                curr += 1
        print(curr)
        out *= curr
    print(out)




def main():
    for _ in range(1):
        solve()


if __name__ == "__main__":
    # Declare any global variables here
    main()

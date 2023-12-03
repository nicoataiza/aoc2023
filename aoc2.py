import sys 
def part_1(line):
    g, p = line.split(':')
    roun = p.split(';')

    for r in roun:
        d = {'red':0,'blue':0,'green':0}
        ball = r.strip().split(',')
        for b in ball:
            num, color = b.split()
            d[color] += int(num)
        if d['red'] > 12 or d['green'] > 13 or d['blue'] >14:
            return (False,0)
    game, num = g.split()
    return (True,int(num))

def part_2(line):
    g, p = line.split(':')
    roun = p.split(';')
    to_bea = {'red':0,'blue':0,'green':0}
    for r in roun:
        d = {'red':0,'blue':0,'green':0}
        ball = r.strip().split(',')
        for b in ball:
            num, color = b.split()
            d[color] += int(num)
        for color in d:
            to_bea[color] = max(to_bea[color],d[color])
    out = 1
    for color in to_bea:
        out *= to_bea[color]
    return out

def solve():
    n = sys.stdin.readlines()
    out = 0
    for game in n: 
        ans = part_2(game)
        out += ans
    print(out)
        

if __name__ == "__main__":
    solve()

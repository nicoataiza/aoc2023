import sys

def part_1_dfs(i,j,arr,n):
    if i < 0 or i > len(n) - 1:
        return ''
    if j < 0 or j > len(n[0]) - 1:
        return '' 
    if not(n[i][j].isnumeric()):
        return ''
    if (i,j) not in arr:
        arr.add((i,j))
        return part_1_dfs(i, j-1, arr, n) + n[i][j] + part_1_dfs(i, j+1, arr, n)
    return ''
    
def part1(n):
    visited = set()
    # i --> row
    max_r = len(n)-1
    max_c = len(n[0])-1
    temp = []
    out = 0
    for i in range(len(n)):
        # j -- > coll
        for j in range(len(n[i])):
            # if special symbols
            if n[i][j] != '.' and not(n[i][j].isnumeric()):
                # get neighhbor 
                # do dfs for each neighbor
                neighbors = set()
                for x in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                    row = i+x[0] if max_r >= i+x[0] >= 0 else max_r if i+x[0] > max_r else 0
                    col = j+x[1] if max_c >= j+x[1] >= 0 else max_c if j+x[1] > max_c else 0
                    neighbors.add((row,col))
                for nn in neighbors:
                    to_add = part_1_dfs(nn[0],nn[1],visited,n)
                    if to_add != '':
                        temp.append(to_add)
    for x in temp:
        out += int(x)
    return out

def part2(n):
    visited = set()
    # i --> row
    max_r = len(n)-1
    max_c = len(n[0])-1
    temp = []
    out = 0
    for i in range(len(n)):
        # j -- > coll
        for j in range(len(n[i])):
            # if special symbols
            if n[i][j] == '*':
                nums = []
                # get neighhbor 
                # do dfs for each neighbor
                neighbors = set()
                for x in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                    row = i+x[0] if max_r >= i+x[0] >= 0 else max_r if i+x[0] > max_r else 0
                    col = j+x[1] if max_c >= j+x[1] >= 0 else max_c if j+x[1] > max_c else 0
                    neighbors.add((row,col))
                for nn in neighbors:
                    to_add = part_1_dfs(nn[0],nn[1],visited,n)
                    if to_add != '':
                        nums.append(to_add)
                if len(nums) == 2:
                    z = 1
                    for num in nums:
                        z *= int(num)
                    temp.append(z)
                    
    for x in temp:
        out += int(x)
    return out

def solve():
    n = sys.stdin.readlines()
    n = [x.strip() for x in n]
    nums = part2(n)
    print(nums)

if __name__ == "__main__":
    solve()

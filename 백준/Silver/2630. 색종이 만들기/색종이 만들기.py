import sys
input = sys.stdin.readline

def A(grid):
    V = 0
    for i in grid:
        for j in i:
            V += j
    
    if V == 0:
        return 1, 0

    elif V == len(grid)*len(grid):
        return 0, 1

    else: 
        lst1, lst2, lst3, lst4 = B(grid)
        c0_1, c1_1 = A(lst1)
        c0_2, c1_2 = A(lst2)
        c0_3, c1_3 = A(lst3)
        c0_4, c1_4 = A(lst4)
        return c0_1 + c0_2 + c0_3 + c0_4, c1_1 + c1_2 + c1_3 + c1_4

def B(grid):
    n = len(grid)
    m = len(grid[0])
    
    half_n = n // 2
    half_m = m // 2
    
    lst1 = [row[:half_m] for row in grid[:half_n]]
    lst2 = [row[half_m:] for row in grid[:half_n]]
    lst3 = [row[:half_m] for row in grid[half_n:]]
    lst4 = [row[half_m:] for row in grid[half_n:]]
    
    return lst1, lst2, lst3, lst4

N = int(input())
grid = []
count0 = 0
count1 = 0

for _ in range(N):
    s = list(map(int,input().split()))
    grid.append(s)

count0, count1 = A(grid)
print(count0)
print(count1)

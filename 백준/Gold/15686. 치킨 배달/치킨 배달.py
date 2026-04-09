import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
house = []
c = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            house.append((i, j))
        elif row[j] == 2:
            c.append((i, j))

c_c = list(combinations(c, M))

min_d = float('inf')

for i in c_c:
    c_d = 0
    for hx, hy in house:
        min_h = float('inf')
        for cx, cy in i:
            dist = abs(hx - cx) + abs(hy-cy)
            min_h = min(min_h, dist)
        c_d += min_h
    min_d = min(min_d, c_d)

print(min_d)
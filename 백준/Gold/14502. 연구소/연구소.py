import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy

N, M = map(int, input().split())
original_map = []
empty_spots = []
virus_spots = [] 

for i in range(N):
    row = list(map(int, input().split()))
    original_map.append(row)
    for j in range(M):
        if row[j] == 0:
            empty_spots.append((i, j))
        elif row[j] == 2:
            virus_spots.append((i, j))

anwser = 0

for walls in combinations(empty_spots, 3): # 빈 곳 중에 3군데 뽑는 코드 자주 쓸 듯 기억해두기
    temp_map = copy.deepcopy(original_map)

    for r, c in walls:
        temp_map[r][c] = 1

    def BFS():
        lst = deque(virus_spots)
        while lst:
            x, y = lst.popleft()
            dit = ((x, y+1),(x, y-1), (x+1, y), (x-1, y))
            for nx, ny in dit:
                if 0 <= nx < N and 0 <= ny < M:
                    if temp_map[nx][ny] == 0:
                        temp_map[nx][ny] = 2  
                        lst.append((nx, ny))

    BFS()
    c_anwser = 0
    for row in temp_map:
        c_anwser += row.count(0)

    if c_anwser > anwser:
        anwser = c_anwser

print(anwser)
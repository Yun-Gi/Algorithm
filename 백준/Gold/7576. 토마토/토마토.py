from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
box = []  
save = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            save.append([i, j])
    box.append(row)


visited = set()
queue = deque(save)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not (0 <= ny < N and 0 <= nx < M):
            continue
        if box[ny][nx] == 0:
            box[ny][nx] = box[y][x] + 1
            queue.append((ny, nx))

days = 0
for row in box:
    for v in row:
        if v == 0:
            print(-1) 
            sys.exit(0)
        days = max(days, v)
print(days - 1)

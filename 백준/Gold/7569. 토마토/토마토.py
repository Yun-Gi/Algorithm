from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
box = []  
save = []
for i in range(H):
    layer = []
    for j in range(N):
        row = list(map(int, input().split()))
        for k in range(M):
            if row[k] == 1:
                save.append([i,j,k])
        layer.append(row)
    box.append(layer)

visited = set()
queue = deque(save)
dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

while queue:
    z, y, x = queue.popleft()
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        if not (0 <= nz < H and 0 <= ny < N and 0 <= nx < M):
            continue
        if box[nz][ny][nx] == 0:
            box[nz][ny][nx] = box[z][y][x] + 1
            queue.append((nz, ny, nx))

days = 0
for layer in box:
    for row in layer:
        for v in row:
            if v == 0:
                print(-1) 
                sys.exit(0)
            days = max(days, v)

print(days - 1)
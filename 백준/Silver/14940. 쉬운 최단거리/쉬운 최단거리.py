from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

result = [[-1 for _ in range(m)] for _ in range(n)]

start_x, start_y = -1, -1
for i in range(n):
    for j in range(m):
        if lst[i][j] == 2:
            start_x, start_y = i, j
            break


q = deque()
q.append((start_x, start_y))
result[start_x][start_y] = 0 
visited = [[False for _ in range(m)] for _ in range(n)]
visited[start_x][start_y] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < n and 0 <= ny < m:
            if lst[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                result[nx][ny] = result[x][y] + 1
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if lst[i][j] == 0: 
            print(0, end=' ')
        else:
            print(result[i][j], end=' ')
    print()
import sys
from collections import deque

input = sys.stdin.readline

def BFS(G, N):
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            
            cnt += 1
            visited[i][j] = True
            queue = deque([(i, j)])

            while queue:
                y, x = queue.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if not(0 <= nx < N and 0 <= ny < N):
                        continue
                    if G[ny][nx] == G[y][x] and not visited[ny][nx]:
                        queue.append((ny, nx))
                        visited[ny][nx] = True
   
    return cnt

N = int(input())
no = []
cw = []
for _ in range(N):
    row = list(input().strip())
    no.append(row)
    row = ['R' if c == 'G' else c for c in row]
    cw.append(row)
print(BFS(no, N), BFS(cw, N))

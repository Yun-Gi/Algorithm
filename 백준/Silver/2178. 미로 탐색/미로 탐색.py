import sys
from collections import deque

input = sys.stdin.readline

def BFS(N, M):
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().strip())))
    
    start = (0,0)
    end = (N-1, M-1)
    queue = deque([(start, 1)])
    visited = set()
    visited.add(start)
   
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (x, y), dist = queue.popleft()
        if (x,y) == end:
            return dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= N-1 and 0 <= ny <= M-1 and (nx, ny) not in visited and lst[nx][ny] == 1:
                visited.add((nx,ny))
                queue.append(((nx, ny), dist + 1))

N, M = map(int, input().split())
print(BFS(N, M))

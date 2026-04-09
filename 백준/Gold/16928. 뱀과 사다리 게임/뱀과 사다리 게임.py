import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
lOrS = [0] * 101
for _ in range(N+M):
    a, b = map(int, input().split())
    lOrS[a] = b

visited = [False] * 101
dice = [1, 2, 3, 4, 5, 6]
queue = deque([1])
visited[1] = True  
moves = 0           


while queue:
    for _ in range(len(queue)):
        x = queue.popleft()
        if x == 100:
            print(moves)
            sys.exit(0)
        for d in dice:
            nx = x + d
            if nx > 100:
                continue
            if lOrS[nx] != 0:
                nx = lOrS[nx]
            if not visited[nx]:
                visited[nx] = True
                queue.append(nx)
    moves += 1

print(-1)

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = {i: [] for i in range(1, N+1)}

for _ in range(N-1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

Ptree = [0] * (N+1)  
visited = [False] * (N+1)
queue = deque([1])
visited[1] = True

while queue:
    x = queue.popleft()
    for i in graph[x]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            Ptree[i] = x

for i in range(2, N+1):
    print(Ptree[i])


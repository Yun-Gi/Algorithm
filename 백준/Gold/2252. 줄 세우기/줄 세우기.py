import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
lst = deque()
anw = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

for i in range(1, N+1):
    if in_degree[i] == 0:
        lst.append(i)

while lst:
    a = lst.popleft()
    anw.append(a)
    for node in graph[a]:
        in_degree[node] -= 1
        if in_degree[node] == 0:
            lst.append(node)

print(*anw)
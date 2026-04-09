import sys
from collections import deque
import heapq 

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

INF = float('inf')
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

pq = []
heapq.heappush(pq, (0, K))
table = [INF] * (V+1)
table[K] = 0

while pq:
    dist, now = heapq.heappop(pq)

    if dist > table[now]:
        continue

    for nn, nc in graph[now]:
        newC = dist + nc      
        if newC < table[nn]:
            table[nn] = newC
            heapq.heappush(pq, (newC, nn))

for i in range(V):
    result = table[i+1]
    if result == float('inf'):
        print("INF")
    else:
        print(result)
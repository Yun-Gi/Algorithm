import sys
from collections import deque
import heapq 
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
graph = {i: [] for i in range(1, n+1)} 
for i in range(n-1):
    p, c, d = map(int, input().split())
    graph[p].append((c, d))
    graph[c].append((p, d))

def dfs(node, current_dist, visited, distance, graph):
    visited[node] = True
    distance[node] = current_dist

    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, current_dist + weight, visited, distance, graph)

distance = [-1] * (n+1)
visited = [False] * (n+1)
dfs(1, 0, visited, distance, graph)
B = 0 
maxV = -1
for i in range(1, n+1):
    if maxV <= distance[i]:
        maxV = distance[i]
        B = i

distance = [-1] * (n+1)
visited = [False] * (n+1)
dfs(B, 0, visited, distance, graph)
print(max(distance))
import sys
import heapq 

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

INF = float('inf') 
table = [INF] * (N + 1) 

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start_node):
    pq = [] 
    
    table[start_node] = 0
    heapq.heappush(pq, (0, start_node)) 

    while pq:
        dist, now = heapq.heappop(pq)

        if table[now] < dist:
            continue

        for neighbor_node, neighbor_cost in graph[now]:
            new_cost = dist + neighbor_cost
            if new_cost < table[neighbor_node]:
                table[neighbor_node] = new_cost
                heapq.heappush(pq, (new_cost, neighbor_node))

dijkstra(start)

print(table[end])

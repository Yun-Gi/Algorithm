import sys
input = sys.stdin.readline
import heapq
INF = sys.maxsize

def dijkstra(start_node, graph_data):
    distances = [INF] * (N + 1)
    distances[start_node] = 0
    queue = []
    
    heapq.heappush(queue, (0, start_node))
    
    while queue:
        current_dist, current_node = heapq.heappop(queue)
        
        if distances[current_node] < current_dist:
            continue
            
        for next_node, weight in graph_data[current_node]:
            cost = current_dist + weight
            
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(queue, (cost, next_node))
                
    return distances

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
back_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    back_graph[v].append((u, w))

come_home = dijkstra(X, graph)

go_party = dijkstra(X, back_graph)

max_time = 0

for i in range(1, N + 1):

    total_time = go_party[i] + come_home[i]
    
    if total_time > max_time:
        max_time = total_time

print(max_time)
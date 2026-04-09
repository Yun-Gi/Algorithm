import sys
import heapq 

input = sys.stdin.readline

N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

INF = float('inf') 


for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

u, v = map(int, input().split())

def dij(sn):
    pq = []
    table = [INF] * (N + 1) 

    table[sn] = 0
    heapq.heappush(pq, (0, sn))

    while pq:
        dist, now = heapq.heappop(pq)
        
        if table[now] < dist:
            continue

        for nn, nc in graph[now]:
            newC = dist + nc
            if newC < table[nn]:
                table[nn] = newC
                heapq.heappush(pq, (newC, nn))
    
    return table

st1 = dij(1)
stU = dij(u)
stV = dij(v)

p1 = st1[u] + stU[v] + stV[N]
p2 = st1[v] + stV[u] + stU[N]


result = min(p1, p2)
if result >= INF:
    print(-1)
else:
    print(result)

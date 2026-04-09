import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

table = [float('inf')] * 1000001

pq = []

table[N] = 0
heapq.heappush(pq, (0, N))

while pq:
    dist, now = heapq.heappop(pq)

    if table[now] < dist:
        continue

    if now == K:
        break

    for n_node, n_cost in ([now-1, 1],[now+1, 1],[2*now, 0]):
        if 0 <= n_node <= 1000000:
            new_cost = dist + n_cost
            if new_cost < table[n_node]:
                table[n_node] = new_cost
                heapq.heappush(pq,(new_cost, n_node))

print(table[K])
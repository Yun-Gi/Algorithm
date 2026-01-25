import heapq
import sys
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    a, b = map(int, input().split())
    lst.append([a, b])

lst.sort()

room = []

heapq.heappush(room, lst[0][1])

for i in range(1, N):
    if room[0] <= lst[i][0]:
        heapq.heappop(room)

    heapq.heappush(room, lst[i][1])

print(len(room))






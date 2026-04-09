import sys
import heapq

input = sys.stdin.readline

minHip = []

N = int(input())

for _ in range(N):
    X = int(input())
    if X == 0:
        if len(minHip) == 0:
            print(0)
        else:
            print(heapq.heappop(minHip))
    else:
        heapq.heappush(minHip, X)

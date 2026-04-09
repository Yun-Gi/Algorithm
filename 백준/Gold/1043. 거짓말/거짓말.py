import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
line = list(map(int, input().split()))
tK = set(line[1:])

p = []
for _ in range(M):
    line = list(map(int, input().split()))
    a = set(line[1:])
    p.append(a)


for _ in range(M):
    for i in p:
        if tK & i:
            tK.update(i)

counter = 0
for i in p:
    if not (tK & i):
        counter += 1
    
print(counter)
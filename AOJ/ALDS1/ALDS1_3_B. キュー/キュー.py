import sys
input = sys.stdin.readline
from collections import deque

n, q = map(int, input().split())
lst = deque()
for _ in range(n):
    a, b = input().split()
    b = int(b)
    lst.append([a, b])

time = 0
while lst:
    if lst[0][1] > q:
        time += q
        lst[0][1] -= q
        lst.append(lst.popleft())
    else:
        time += lst[0][1]
        print(lst[0][0], end=" ")
        print(time)
        lst.popleft()
           





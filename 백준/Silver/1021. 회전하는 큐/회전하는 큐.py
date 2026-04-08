import sys
input = sys.stdin.readline
from collections import deque

class cirQue:
    def __init__(self, N):
        self.N = N
        self.lst = deque(range(1, N + 1))


    def one(self):
        if self.lst:
            self.lst.popleft()

    def two(self):
        if self.lst:
            x = self.lst.popleft()
            self.lst.append(x)

    def three(self):
        if self.lst:
            x = self.lst.pop()
            self.lst.appendleft(x)

N, M = map(int, input().split())
targets = list(map(int, input().split()))

cq = cirQue(N)
count = 0
for target in targets:
    idx = cq.lst.index(target)
    mid = len(cq.lst) // 2
    if cq.lst[0] == target:
        cq.one()
    elif idx <= mid:
        while cq.lst[0] != target:
            cq.two()
            count += 1
        cq.one()
    elif idx > mid:
        while cq.lst[0] != target:
            cq.three()
            count += 1
        cq.one()

print(count)
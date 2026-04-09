import sys
from collections import deque

input = sys.stdin.readline

def BFS(S, E):
    if S == E:
        return 0

    next = deque([S])
    visited = set()
    visited.add(S)
    counter = 0

    while next:
        counter += 1
        for _ in range(len(next)):
            x = next.popleft()
            for nx in (x-1, x+1, x*2):
                if nx == E:
                    return counter
                if 0 <= nx <= 100000 and nx not in visited:
                    visited.add(nx)
                    next.append(nx)
    return -1

N, K = map(int, input().split())
print(BFS(N, K))
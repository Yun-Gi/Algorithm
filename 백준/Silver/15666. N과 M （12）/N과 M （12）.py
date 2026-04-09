import sys
input = sys.stdin.readline
from collections import deque

def DFS(start, depth):
    if depth == M:
        t = tuple(col)
        if t not in dup:
            print(*t)
            dup.add(t)
            return   
        else:
            return
        
    else:
        for i in range(start, N):
            if not visited[i]:
                col.append(lst[i])
                DFS(i,depth+1)
                col.pop()



N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()
visited = [False]*N
col = []
dup = set()

DFS(0, 0)

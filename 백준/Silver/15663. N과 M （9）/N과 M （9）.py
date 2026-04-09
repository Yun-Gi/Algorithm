import sys
input = sys.stdin.readline
from collections import deque

def DFS(depth):
    if depth == M:
        t = tuple(col)
        if t not in dup:
            print(*t)
            dup.add(t)
            return   
        else:
            return
        
    else:
        for i in range(0, N):
            if not visited[i]:
                col.append(lst[i])
                visited[i] = True
                DFS(depth+1)
                col.pop()
                visited[i] = False



N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()
visited = [False]*N
col = []
dup = set()

DFS(0)
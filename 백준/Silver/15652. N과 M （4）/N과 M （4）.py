import sys
input = sys.stdin.readline

def DFS(start, depth):
    if depth == M:
        print(*lst)
        return

    else:
        for i in range(start, N+1):
            lst.append(i)
            DFS(i, depth+1)
            lst.pop()

N, M = map(int, input().split())
lst = []
DFS(1,0)

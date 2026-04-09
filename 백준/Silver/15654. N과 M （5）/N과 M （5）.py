import sys
input = sys.stdin.readline

def DFS(depth):
    if depth == M:
        print(*lst)
        return

    else:
        for i in range(0, N):
            if not visited[i]:
                lst.append(qwer[i])
                visited[i] = True
                DFS(depth+1)
                lst.pop()
                visited[i] = False

N, M = map(int, input().split())
qwer = list(map(int, input().split()))
qwer.sort()
visited = [False]*N
lst = []
DFS(0)
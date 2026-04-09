import sys
input = sys.stdin.readline

def dfs(grid, i, j, N, M):
    lst = [(i, j)]
    while lst:
        x, y = lst.pop()
        if x < 0 or x >= N or y < 0 or y >= M or grid[x][y] != 1:
            continue
        grid[x][y] = -1
        lst.append((x - 1, y))
        lst.append((x + 1, y))
        lst.append((x, y - 1))
        lst.append((x, y + 1)) 

T = int(input())

for _ in range(T):
    M, N, K = map(int,input().split())
    lst = [[0] * M for _ in range(N)]
    counter = 0
    for _ in range(K):
        X, Y = map(int,input().split())
        lst[Y][X] = 1
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                dfs(lst,i,j,N,M)
                counter += 1
    print(counter)

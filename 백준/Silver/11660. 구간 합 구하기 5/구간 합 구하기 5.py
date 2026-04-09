import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
dp = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    lst.append(list(map(int, input().split())))

dp[0][0] = lst[0][0]

for i in range(1, N):
    dp[i][0] = dp[i-1][0] + lst[i][0]
    dp[0][i] = dp[0][i-1] + lst[0][i]

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + lst[i][j]
        
for _ in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    if x1 == 1 and y1 == 1:
        result = dp[x2-1][y2-1]
    elif x1 == 1:
        result = dp[x2-1][y2-1] - dp[x2-1][y1-2]
    elif y1 == 1:
        result = dp[x2-1][y2-1] - dp[x1-2][y2-1]
    else: 
        result = dp[x2-1][y2-1] - dp[x1-2][y2-1] - dp[x2-1][y1-2] + dp[x1-2][y1-2]
    print(result)
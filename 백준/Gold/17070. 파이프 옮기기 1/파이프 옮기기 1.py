import sys

input = sys.stdin.readline

N = int(input())
house = []
dp = [[[0]*N for _ in range(N)] for _ in range(3)]
for i in range(N):
    house.append(list(map(int, input().split())))

dp[0][0][1] = 1 

for j in range(2, N):
    if house[0][j] == 0:
        dp[0][0][j] = dp[0][0][j-1]
    else:
        break

for i in range(1, N):
    for j in range(1, N):
        if house[i][j] == 1:
            continue
        dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
        dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
        if house[i-1][j] == 0 and house[i][j-1] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])
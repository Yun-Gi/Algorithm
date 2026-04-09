import sys
input = sys.stdin.readline

N = int(input())
lst = []
dp = [[1001,1001,1001] for _ in range(N)]
result = 0

for _ in range(N):
    r,g,b = map(int, input().split())
    lst.append([r,g,b])

# 0->빨 1->초 2->파
dp[1][0] = lst[1][0] + min(lst[0][1], lst[0][2])
dp[1][1] = lst[1][1] + min(lst[0][0], lst[0][2])
dp[1][2] = lst[1][2] + min(lst[0][0], lst[0][1])

for i in range(2, N):
    for j in range(3):
        dp[i][j] = lst[i][j] + min(dp[i-1][j-1],dp[i-1][j-2])

print(min(dp[N-1][0],dp[N-1][1],dp[N-1][2]))
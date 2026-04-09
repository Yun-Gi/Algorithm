import sys

input = sys.stdin.readline

N1 = input().strip()
N2 = input().strip()
dp = [[0 for _ in range(len(N2)+1)] for _ in range(len(N1)+1)]

for i in range(1, len(N1) + 1):
    for j in range(1, len(N2) + 1):
        if N1[i-1] == N2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(N1)][len(N2)])

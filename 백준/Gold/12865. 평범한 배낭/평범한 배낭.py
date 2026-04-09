import sys

input = sys.stdin.readline

N, K = map(int, input().split())
lst = []
dp = [0 for _ in range(K+1)]
for _ in range(N):
    W, V = map(int, input().split())
    lst.append([W, V])


for W, V in lst:
    for j in range(K, W-1, -1):
        dp[j] = max(dp[j], dp[j - W] + V)

print(dp[K])

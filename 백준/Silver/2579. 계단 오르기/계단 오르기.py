import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
dp = [0] * N

if N == 1:
    print(lst[0])
    sys.exit()

elif N == 2:
    print(lst[0] + lst[1])
    sys.exit()

dp[0] = lst[0]
dp[1] = lst[0] + lst[1] if N > 1 else lst[1]
dp[2] = max(lst[0] + lst[2], lst[1] + lst[2]) if N > 2 else lst[2]

for i in range(3, N):
    dp[i] = max(dp[i-2] + lst[i], dp[i-3]+lst[i-1]+lst[i])

print(dp[N-1])
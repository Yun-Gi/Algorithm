import sys
input = sys.stdin.readline


T = int(input())
dp=[0]*100
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 3
dp[6] = 4
dp[7] = 5
dp[8] = 7
dp[9] = 9

for _ in range(T):
    N = int(input())
    for i in range(10,N):
        dp[i] = dp[i-1] + dp[i-5]

    print(dp[N-1])

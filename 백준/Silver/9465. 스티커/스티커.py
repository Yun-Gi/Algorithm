import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    lst = []
    for i in range(2):
        lst.append(list(map(int,input().split())))

    dp = [[0, 0] for _ in range(N)]

    dp[0][0] = lst[0][0]
    dp[0][1] = lst[1][0]

    if N != 1:
        dp[1][0] = lst[0][1] + dp[0][1]
        dp[1][1] = lst[1][1] + dp[0][0]


    for i in range(2, N):
        dp[i][0] = lst[0][i] + max(dp[i-1][1], dp[i-2][0], dp[i-2][1])
        dp[i][1] = lst[1][i] + max(dp[i-1][0], dp[i-2][0], dp[i-2][1])
    print(max(dp[N-1]))
        
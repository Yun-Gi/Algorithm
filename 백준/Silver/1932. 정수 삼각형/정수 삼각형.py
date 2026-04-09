import sys
input = sys.stdin.readline

N = int(input())
lst = []
dp = [[0 for j in range(i+1)] for i in range(N) ]

for i in range(N):
    lst.append(list(map(int,input().split())))

dp[0][0] = lst[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = lst[i][j] + dp[i-1][0]

        elif j == i:
            dp[i][j] = lst[i][j] + dp[i-1][j-1]

        else:    
            dp[i][j] = lst[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[N-1]))
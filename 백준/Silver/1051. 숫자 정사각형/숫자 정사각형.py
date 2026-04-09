import sys
input = sys.stdin.readline

N, M = map(int,input().split())

squB = max(N, M) # 그리디하게 하기 위해 가능한 가장 큰 너비 부터 서치
lst = [list(map(int, input().strip())) for _ in range(N)]
end = False

while not end:
    # 2중 반복문으로 돌면서 서치
    for i in range(N-squB+1):
        for j in range(M-squB+1):
            if lst[i][j] == lst[i][j+squB-1] == lst[i+squB-1][j] == lst[i+squB-1][j+squB-1]:
                end = True
    squB -= 1

squB += 1
print(squB ** 2)
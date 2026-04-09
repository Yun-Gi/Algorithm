import sys
input = sys.stdin.readline


N, M = map(int,input().split())
lst = list(map(int,input().split()))
sub_lst = []
sum = 0

for i in range(0,N):
    sum += lst[i]
    sub_lst.append(sum)

for _ in range(M):
    i, j = map(int,input().split())
    max = sub_lst[j-1]
    if i-2 < 0:
        min = 0
    else:
        min = sub_lst[i-2]
    print(max-min)
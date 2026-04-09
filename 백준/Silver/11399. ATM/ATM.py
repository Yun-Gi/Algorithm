import sys
input = sys.stdin.readline

N = int(input())
lst = []

lst = list(map(int, input().split()))

lst.sort()
sum = 0

for i in range(N):
    for j in range(i+1):
        sum += lst[j]

print(sum)

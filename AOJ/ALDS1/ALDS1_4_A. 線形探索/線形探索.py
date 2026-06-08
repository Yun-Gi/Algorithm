import sys
input = sys.stdin.readline

count = 0
n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

for i in T:
    for j in S:
        if i == j:
            count += 1
            break

print(count)










           





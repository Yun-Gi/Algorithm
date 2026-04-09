import sys
input = sys.stdin.readline

MAX_N = 40

count_0 = [0] * (MAX_N + 1)
count_1 = [0] * (MAX_N + 1)

count_0[0] = 1
count_1[0] = 0
count_0[1] = 0
count_1[1] = 1

for i in range(2, MAX_N + 1):
    count_0[i] = count_0[i-1] + count_0[i-2]
    count_1[i] = count_1[i-1] + count_1[i-2]

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_0[N], count_1[N])
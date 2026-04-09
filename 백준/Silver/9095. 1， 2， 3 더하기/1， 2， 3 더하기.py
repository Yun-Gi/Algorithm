import sys
input = sys.stdin.readline


T = int(input())
lst = [0] * 11

lst[0] = 1
lst[1] = 2
lst[2] = 4

for i in range(3,11):
    lst[i] = lst[i-3] + lst[i-2] + lst[i-1]

for i in range(T):
    N = int(input())
    print(lst[N-1])
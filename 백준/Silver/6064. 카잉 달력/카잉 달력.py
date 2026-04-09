import sys
import math

input = sys.stdin.readline

def cal(M, N, x, y):
    J = M * N // math.gcd(M, N)
    for i in range(x, J+1, M):
        if (i - y) % N == 0:
           return i
    return -1

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(cal(M, N, x, y))
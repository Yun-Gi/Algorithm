import sys
input = sys.stdin.readline

N, K = map(int,input().split())
coin = [0] * N
coin_sum = 0

for i in range(N):
    coin[i] = int(input())

for i in range(N-1,-1,-1):
    coin_sum += K // coin[i]
    K %= coin[i]

print(coin_sum)
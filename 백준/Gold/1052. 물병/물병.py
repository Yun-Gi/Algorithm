import sys
input = sys.stdin.readline

N, K = map(int, input().split())

bot = bin(N)
count = 0

while K < bot.count("1"):
    N += 1
    bot = bin(N)
    count += 1
print(count)
    
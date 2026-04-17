import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
bigger = max(X, Y)
smaller = min(X, Y)
r = bigger % smaller

while r != 0:
   bigger = smaller
   smaller = r
   r = bigger % smaller

print(smaller)

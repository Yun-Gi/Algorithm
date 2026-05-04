import sys
input = sys.stdin.readline

n = int(input())
smaller = float('INF')
saidai_rieki = float('-INF')
for _ in range(n):
    x = int(input())
    rieki = x - smaller
    if rieki > saidai_rieki:
        saidai_rieki = rieki
    if smaller > x:
        smaller = x
    
print(saidai_rieki)

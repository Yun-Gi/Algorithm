import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int,input().split())
    n = int(input())
    count = 0
    for i in range(n):
        c1, c2, r = map(int, input().split())
        in_start = (x1 - c1)**2 + (y1 - c2)**2 < r**2
        in_end = (x2 - c1)**2 + (y2 - c2)**2 < r**2
        if in_start != in_end:
            count += 1
    print(count)
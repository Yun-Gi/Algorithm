import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))
stack = []
anw = [0] * N

for i in range(N-1, -1, -1):
    while stack and stack[-1][1] < tower[i]:
        idx, height = stack.pop()
        anw[idx] = i + 1

    stack.append((i,tower[i]))

print(*anw)
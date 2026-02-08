import sys
input = sys.stdin.readline

N = int(input())
queens = [0] * N
anw = 0

def sol(x):
    if x == N:
        global anw
        anw += 1
        return
    for col in range(N):
        queens[x] = col
        if can(x):
            sol(x + 1)

def can(x):
    for i in range(x):
        if queens[x] == queens[i]:
            return False
        if abs(queens[x] - queens[i]) == abs(x - i):
            return False
    return True

sol(0)
print(anw)
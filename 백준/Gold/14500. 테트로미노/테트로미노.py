import sys
input = sys.stdin.readline

shapes = [
    # I (2가지)
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(2,0),(3,0)],

    # O (1가지)
    [(0,0),(0,1),(1,0),(1,1)],

    # T (4가지)
    [(0,0),(0,1),(0,2),(1,1)],
    [(0,1),(1,0),(1,1),(1,2)],
    [(0,0),(1,0),(2,0),(1,1)],
    [(0,1),(1,1),(2,1),(1,0)],

    # Z (4가지)
    [(0,1),(0,2),(1,0),(1,1)],
    [(0,0),(1,0),(1,1),(2,1)],

    [(0,0),(0,1),(1,1),(1,2)],
    [(0,1),(1,0),(1,1),(2,0)],

    # L (8가지)
    [(0,0),(1,0),(2,0),(2,1)],
    [(0,0),(0,1),(0,2),(1,0)],
    [(0,0),(0,1),(1,1),(2,1)],
    [(1,0),(1,1),(1,2),(0,2)],

    [(0,1),(1,1),(2,1),(2,0)],
    [(0,0),(1,0),(1,1),(1,2)],
    [(0,0),(1,0),(2,0),(0,1)],
    [(0,0),(0,1),(0,2),(1,2)],
]

N, M = map(int, input().split())
board = []
maxN = -1

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

for x in range(N):
    for y in range(M):
        for a, b, c, d in shapes:
            coords = [
                (x + a[0], y + a[1]),
                (x + b[0], y + b[1]),
                (x + c[0], y + c[1]),
                (x + d[0], y + d[1])
            ]
            total = 0
            valid = True
            for nx, ny in coords:
                if not(0 <= nx < N and 0 <= ny < M):
                    valid = False
                    break
                total += board[nx][ny]
            
            if valid and total > maxN:
                maxN = total

print(maxN)
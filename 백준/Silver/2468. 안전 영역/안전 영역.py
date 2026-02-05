import sys
input = sys.stdin.readline

N = int(input())
lst = []
max_height = 0

for _ in range(N):
    row = list(map(int, input().split()))
    lst.append(row)
    max_height = max(max_height, max(row))

maxi = 1

for i in range(1, max_height):
    visit = [[False] * N for _ in range(N)]
    direction = ((1,0), (-1,0), (0, 1), (0,-1))
    ryoiki = 0
    for x in range(N):
        for y in range(N):
            if lst[x][y] > i and visit[x][y] == False:
                lst1 = [(x, y)]
                visit[x][y] = True
                while lst1:
                    curr_x, curr_y = lst1.pop()
                    for dx, dy in direction:
                        nx, ny = curr_x + dx, curr_y + dy
                        if nx >= 0 and nx < N and ny >= 0 and ny < N and lst[nx][ny] > i and not visit[nx][ny]:
                            visit[nx][ny] = True
                            lst1.append((nx, ny))

                ryoiki += 1
    maxi = max(ryoiki, maxi)

print(maxi)
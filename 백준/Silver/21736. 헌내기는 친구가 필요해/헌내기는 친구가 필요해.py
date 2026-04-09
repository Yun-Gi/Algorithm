import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
start = None
counter = 0

for i in range(N):
    row = input()
    lst.append(list(row))  # 각 줄을 리스트로 저장
    if 'I' in row:
        start = (i, row.index('I'))  # I의 좌표 저장

visited = set()
dfs = [start]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while dfs:
    x, y = dfs.pop()
    if (x, y) not in visited:
        visited.add((x,y))
        if lst[x][y] == 'P':
            counter += 1
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and lst[nx][ny] != 'X' and (nx, ny) not in visited:
                dfs.append((nx, ny))

if counter == 0:
    print("TT")
else:
    print(counter)
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

lst = []
result = []
counter = 0

for _ in range(N):
    lst.append(list(map(int, input().strip())))

visited = set()
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    for j in range(len(lst[i])):
        if lst[i][j] == 1 and (i, j) not in visited:
            count = 1
            Queue = deque([(i, j)])
            visited.add((i, j))
            while Queue:
                x, y = Queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < len(lst[i]) and (nx, ny) not in visited and lst[nx][ny] == 1:
                        visited.add((nx, ny))
                        Queue.append((nx, ny))
                        count += 1
            result.append(count)
            counter += 1

print(counter)
result.sort()
for i in result:
    print(i)
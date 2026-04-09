import sys
input = sys.stdin.readline
from collections import deque

A, B = map(int, input().split())

visited = {A}
queue = deque([A])
counter = 1

while queue:
    for _ in range(len(queue)):
        x = queue.popleft()
        if x == B:
            print(counter)
            sys.exit()
        lst = [x*2, x*10+1]
        for i in lst:
            if i not in visited and i <= B:
                queue.append(i)
                visited.add(i)
    counter += 1   

print(-1)
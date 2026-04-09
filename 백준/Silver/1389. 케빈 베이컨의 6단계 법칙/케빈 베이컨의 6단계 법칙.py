import sys
input = sys.stdin.readline
from collections import deque

min_counter = float('inf') # 케빈 베이컨 수 최소 값 저장용

N, M = map(int,input().split())

comu = {} # 그래프 넣을 딕셔너리

for i in range(1, N+1):
    comu[i] = []

for _ in range(M): # 그래프에 값 삽입
    x, y = map(int,input().split())
    comu[x].append(y)
    comu[y].append(x)

def bfs(start):
    distances = {i: float('inf') for i in range(1, N + 1)}
    distances[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in comu[node]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    
    return sum(distances.values())

# 케빈 베이컨 수가 가장 작은 유저 찾기
min_bacon = float('inf')
min_user = -1

for i in range(1, N + 1):
    bacon = bfs(i)
    if bacon < min_bacon:
        min_bacon = bacon
        min_user = i

print(min_user)

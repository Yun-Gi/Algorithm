import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
front = 0
rear = N - 1
min = [front, rear, INF] # 최소값일때 프론트위치, 리어 위치, 최소값

while front < rear:
    if min[2] > abs(lst[front] + lst[rear]):
        min[0] = front
        min[1] = rear
        min[2] = abs(lst[front] + lst[rear])

        if 0 == lst[front] + lst[rear]:
            break
    if lst[front] + lst[rear] < 0:
        front += 1
    else:
         rear -= 1

print(lst[min[0]], lst[min[1]])
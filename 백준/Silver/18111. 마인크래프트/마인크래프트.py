import sys
input = sys.stdin.readline

N, M, B = map(int,input().split())

array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

height = 0
timer = float('inf')

for i in range(257):
    remove = 0
    add = 0
    for j in range(N):
        for k in range(M):
            if array[j][k] > i:
                remove += array[j][k] - i
            else:
                add += i - array[j][k]

    if remove + B >= add:
        time = remove * 2 + add
        if time < timer or (time == timer and i > height):
            timer = time
            height = i

print(timer, height)

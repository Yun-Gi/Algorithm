import sys
input = sys.stdin.readline

n, k = map(int, input().split())
w = []

for _ in range(n):
    w.append(int(input()))

left = 0
right = 1000000000
answer = right

while left <= right:
    mid = (left + right) // 2
    truck = 1
    load = 0
    dekiru = True

    for weight in w:
        if weight > mid:
            dekiru = False
            break
        if load + weight > mid:
            truck += 1
            load = weight
            if truck > k:
                dekiru = False
                break
        else:
            load += weight
    
    if dekiru:
        answer = mid
        right = mid - 1

    else:
        left = mid + 1

print(answer)









           





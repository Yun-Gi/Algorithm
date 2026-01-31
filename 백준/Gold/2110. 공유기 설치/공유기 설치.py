import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()
start = 1
end = house[-1] - house[0] 
result = 0

def check():
    last_install = house[0]
    install = 1
    for i in range(1, N):
        if house[i] - last_install >= mid:
            last_install = house[i]
            install += 1
    
    if install >= C:
        return False
    else:
        return True

while start <= end:
    mid = (start + end) // 2
    if check():
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
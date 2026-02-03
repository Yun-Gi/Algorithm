import sys
input = sys.stdin.readline

N = int(input()) # 지방 수
limit = list(map(int, input().split())) # 요청 예산
M = int(input()) # 총 예산

# 어차피 지방 순서가 중요한 문제가 아니기에 정렬
limit.sort()
start = 1
end = limit[-1]
anw = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for value in limit:
        if value <= mid:
            total += value
        else:
            total += mid
    if total > M:
        end = mid - 1
    else:
        anw = mid
        start = mid + 1
        

print(anw)
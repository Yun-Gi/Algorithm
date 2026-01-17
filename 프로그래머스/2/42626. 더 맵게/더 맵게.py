import heapq

def solution(scoville, K):
    lst = []
    cnt = 0
    for i in scoville:
        heapq.heappush(lst, i)
    while lst[0] < K and len(lst) > 1:
        a = heapq.heappop(lst)
        b = heapq.heappop(lst)
        c = a + b*2
        cnt += 1
        heapq.heappush(lst, c)
    
    if lst[0] < K:
        return -1
    return cnt
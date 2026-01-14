import heapq

def solution(n, works):
    answer = 0
    if n >= sum(works):
        return 0
    
    heap = []
    for i in works:
        heapq.heappush(heap,-i)
    
    for i in range(n):
        bigNum = heapq.heappop(heap)
        bigNum += 1
        heapq.heappush(heap, bigNum)
            
    for i in heap:
        answer += i**2
    
    return answer

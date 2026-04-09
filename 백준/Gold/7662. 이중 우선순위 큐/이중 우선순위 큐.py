import heapq

T = int(input())
for _ in range(T):
    k = int(input())
    min_heap, max_heap = [], []
    counter = {}
    size = 0
    for _ in range(k):
        c, n = input().split()
        n = int(n)
        if c == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            counter[n] = counter.get(n, 0) + 1
            size += 1
        else:
            if n == 1:
                while max_heap and counter.get(-max_heap[0], 0) == 0:
                    heapq.heappop(max_heap)
                
                if max_heap:
                    val = -heapq.heappop(max_heap)
                    counter[val] -= 1
                    size -= 1
            else:
                while min_heap and counter.get(min_heap[0], 0) == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    val = heapq.heappop(min_heap)
                    counter[val] -= 1
                    size -= 1
                    
    while max_heap and counter.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)
    while min_heap and counter.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)

    if size != 0:
        print(max_heap[0] * -1, min_heap[0])
    else:
        print('EMPTY')
import sys

input = sys.stdin.readline

def heap_in(heap, x): # 힙안에 넣고 정렬
    heap.append(x)
    i = len(heap) - 1 # x의 인덱스 값
    xp = abs(x)  # 비교할 절대값을 가지는 용도의 x프라임 생성
   
    while True:
        if i == 0:
            break

        j = (i - 1) // 2
        y = heap[j] # x의 부모노드
        yp = abs(y) # y의 절댓값

        if xp < yp or (xp == yp and x < y):
            heap[i] = y
            i = j
        else:
            break
    
    heap[i] = x

def heap_out(heap): # 힙에서 노드값 제거
    if len(heap) == 0:
        return 0
        
    root = heap[0]
    last = heap.pop()

    if len(heap) == 0:
        return root

    heap[0] = last
    heap_up(heap)
    return root

def heap_up(heap): # 노드값이 빠진 힙 정렬 
    i = 0
    n = len(heap)
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < n and (abs(heap[left]) < abs(heap[smallest]) or (abs(heap[left]) == abs(heap[smallest]) and heap[left] < heap[smallest])):
            smallest = left
        if right < n and (abs(heap[right]) < abs(heap[smallest]) or (abs(heap[right]) == abs(heap[smallest]) and heap[right] < heap[smallest])):
            smallest = right

        if smallest == i:
            break

        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest



N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        print(heap_out(heap))
    else:
        heap_in(heap, x)
import sys
input = sys.stdin.readline

def heap_push(heap, value):
    heap.append(value)
    index = len(heap) - 1
    while index > 0:
        parent = (index - 1) // 2
        if heap[index] > heap[parent]:
            heap[index], heap[parent] = heap[parent], heap[index]
            index = parent
        else:
            break

def heapify_down(heap, index):
    n = len(heap)
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < n and heap[left] > heap[largest]:
        largest = left
    if right < n and heap[right] > heap[largest]:
        largest = right

    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        heapify_down(heap, largest)

def extract_max(heap):
    if not heap:
        print(0)
        return
    max_val = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    heapify_down(heap, 0)
    print(max_val)

N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    if num == 0:
        extract_max(heap)
    else:
        heap_push(heap, num)
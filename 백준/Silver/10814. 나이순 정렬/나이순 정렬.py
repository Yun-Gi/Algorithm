def merge_sort(arr,key):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left,key)
    right = merge_sort(right,key)

    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

N = int(input())

lst = [[] for _ in range(N)]


for j in range(N):
    num, name = input().split()
    num=int(num)
    lst[j].append(num)
    lst[j].append(name)


result = merge_sort(lst,0)

for i in result:
    print(f"{i[0]} {i[1]}")

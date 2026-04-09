def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1
        elif left[i][0] == right[j][0]:
            if left[i][1] <= right[j][1]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


N = int(input())

lst = [[] for _ in range(N)]

for i in range(N):
    X, Y = map(int,input().split())
    lst[i] = [X,Y]

result = merge_sort(lst)

for i in result:
    print(f"{i[0]} {i[1]}")
def divide(a):
    l = len(a)
    if l<=1:
        return a
    front = divide(a[:l//2])
    back = divide(a[l//2:])
    
    return conquer(front, back)

def conquer(a, b):
    result = []
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1
    if i<len(a):
        result.extend(a[i:])
    if j<len(b):
        result.extend(b[j:])
    return result

def binary_search(a, x, low=0, high=None):
    if high is None:
        high = len(a) - 1

    if low > high:
        return False

    mid = (low + high) // 2 

    if a[mid] == x: 
        return True
    elif a[mid] < x:  
        return binary_search(a, x, mid + 1, high)
    else:
        return binary_search(a, x, low, mid - 1)

    

N = int(input())
lst = list(map(int,input().split()))

M = int(input())
lst2 = list(map(int,input().split()))

lst = divide(lst)

for i in lst2:
    re = binary_search(lst,i)
    if re == True:
        print(1)
    else:
        print(0)

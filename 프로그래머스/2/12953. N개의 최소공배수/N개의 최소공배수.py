def solution(arr):
    answer = 0
    num = arr[0]
    for i in range(1, len(arr)):
        a = Euclidean(num, arr[i])
        num = (num * arr[i]) / a
    answer = num
    return answer

def Euclidean(a, b):
    while b != 0:
        a, b = b, a%b
    return a
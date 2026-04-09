import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst2 = lst[:]
result = [None] * len(lst)

lst2 = sorted(set(lst2))
dic = {value: index for index, value in enumerate(lst2)}

for i in range(len(lst)):
    result[i] = dic[lst[i]]

for i in result:
    print(i, end=" ")
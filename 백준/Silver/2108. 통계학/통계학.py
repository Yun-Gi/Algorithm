import sys
from collections import Counter

def around(N):
    if N >= 0: 
        if N - int(N) >= 0.5:
            return int(N)+1
        else: return int(N)
    else:
        if N - int(N) < -0.5:
            return int(N)-1
        else: return int(N)

def frequ(arr):
    frequency = Counter(arr)
    most_common = frequency.most_common()
    max_freq = most_common[0][1]
    modes = [num for num, freq in most_common if freq == max_freq]

    if len(modes) > 1:
        mode = sorted(modes)[1]
    else:
        mode = modes[0]
    return mode
N = int(sys.stdin.readline().strip())
lst = []

for i in range(N):
    lst.append(int(sys.stdin.readline().strip()))

lst.sort()
print(around(sum(lst)/N))
print(lst[(N//2)])
print(frequ(lst))
print(lst[N-1]-lst[0])
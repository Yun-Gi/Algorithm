import sys
from collections import deque

input = sys.stdin.readline

N = input().strip()
N = list(N)
bn = -1
sum = 0

for i in range(len(N)):
    if N[i] == '*':
        bn = i
    else:
        N[i] = int(N[i])

for i in range(len(N)):
    if i != bn and i != len(N)-1:
        if i % 2 == 0:
            sum += N[i]
        else:
            sum += 3*N[i]

if N[-1] == 0:
    N[-1] = 10
    
if bn % 2 == 0:
    for i in range(10):
        if N[-1] == 10 - (sum + i)%10:
            print(i)
            break
else:
    for i in range(10):
        if N[-1] == 10 - (sum + 3*i)%10:
            print(i)
            break
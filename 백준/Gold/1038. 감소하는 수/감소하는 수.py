import sys
input = sys.stdin.readline

lst = []
def dfs(cNum):
    lst.append(cNum)
    lDigit = cNum % 10
    for i in range(lDigit):
        nNum = cNum * 10 + i
        dfs(nNum)

for i in range(10):
    dfs(i)

N = int(input())
lst.sort()

if N >= len(lst):
    print(-1)
else:
    print(lst[N])
import ast
from collections import deque

T = int(input())
for i in range(T):
    S = input().strip()
    P = list(S)
    N = int(input())
    inLst = input().strip()
    lst = deque(ast.literal_eval(inLst))
    
    checkE = False
    checkR = -1 # -1이 정상 1이 뒤집힌 상태
    for j in P:
        if j == 'R':
            checkR *= -1
        
        if j == 'D':
            if len(lst) == 0:
                checkE = True
                break
            else:
                if checkR == -1:
                    lst.popleft()
                else:
                    lst.pop()

    if checkE:
        print('error')
    else:
        lst = list(lst)
        if checkR == 1:
            lst.reverse()
        print("[" + ",".join(map(str, lst)) + "]")
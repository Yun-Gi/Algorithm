from collections import deque
import sys
input = sys.stdin.readline

def D(n):
    return (2 * n) % 10000

def S(n):
    return 9999 if n == 0 else n - 1

def L(n):
    return (n % 1000) * 10 + (n // 1000)

def R(n):
    return (n % 10) * 1000 + (n // 10)

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    visited = [False]*10000
    parent  = [-1]    * 10000 
    op      = ['']    * 10000

    Q = deque([A])
    visited[A] = True
    
    while Q:
        cur = Q.popleft()
        if cur == B:
            break
        
        for fn, ch in ((D,'D'), (S,'S'), (L,'L'), (R,'R')):
            nxt = fn(cur)
            if not visited[nxt]:
                visited[nxt] = True
                parent[nxt] = cur
                op[nxt] = ch
                Q.append(nxt)
    seq = []
    x = B
    while x != A:
        seq.append(op[x])
        x = parent[x]
    seq.reverse()

    print(''.join(seq))

import sys

input = sys.stdin.readline

def Z(N, r, c):
    result = 0
    sizex = 2**(N-1)
    sizey = 2**(N-1)

    while N>0:
        N -= 1
        if c<sizex and r<sizey:
            sizex -= 2**(N-1)
            sizey -= 2**(N-1)
        elif c>=sizex and r<sizey:
            result += 4**N
            sizex += 2**(N-1)
            sizey -= 2**(N-1)
        elif c<sizex and r>=sizey:
            result += 2*(4**N)
            sizex -= 2**(N-1)
            sizey += 2**(N-1)
        else:
            result += 3*(4**N)
            sizex += 2**(N-1)
            sizey += 2**(N-1)
        
    return result
    
N, r, c = map(int, input().split())

print(Z(N, r, c))

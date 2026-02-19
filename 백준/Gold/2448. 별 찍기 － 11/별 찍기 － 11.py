import sys
input = sys.stdin.readline


N = int(input())

def A(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]
    else:
        star = A(n//2)
        L = []
        
        for s in star:
            L.append(" " * (n//2) + s + " " * (n//2))
        for s in star:
            L.append(s + " " + s)
        return L

print('\n'.join(A(N)))
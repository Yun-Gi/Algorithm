import sys
input = sys.stdin.readline


T = int(input())


for _ in range(T):
    n = int(input().strip())
    clothes = {}
    result = 1
    
    for _ in range(n):
        name, kind = input().strip().split()
        if kind in clothes:
            clothes[kind].append(name)
        else:
            clothes[kind] = [name]

    for kind, items in clothes.items():
        result *= (len(items)+1)
    result -= 1
    print(result)
    
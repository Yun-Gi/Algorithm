import sys
input = sys.stdin.readline

N, M = map(int,input().split())
pokemon = {}
pokemon_reverse = {}

for i in range(N):
    name = input().strip()
    pokemon[i+1] = name
    pokemon_reverse[name] = i+1

for j in range(M):
    C = input().strip()
    if C.isalpha():
        print(pokemon_reverse[C])
    else:
        print(pokemon[int(C)])
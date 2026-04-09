import sys
input = sys.stdin.readline

N, M = map(int,input().split())
pokemon_reverse = {}
result = []

for _ in range(N+M):
    name = input().strip()
    if name in pokemon_reverse:
        pokemon_reverse[name] += 1
    else:
        pokemon_reverse[name] = 1

for key, value in pokemon_reverse.items():
    if value == 2:
        result.append(key)

result.sort()
print(len(result))
for i in result:
    print(i)
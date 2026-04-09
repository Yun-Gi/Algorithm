result = []
N = int(input())
lst = []
for i in range(N):
    S, E = map(int, input().split())
    lst.append([S,E])

lst.sort(key=lambda x: (x[1], x[0]))

rel = 0
for i in lst:
    if i[0] >= rel:
        result.append(i)
        rel = i[1]

print(len(result))
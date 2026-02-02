import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
graph = []

for _ in range(E):
    a, b, c = map(int, input().split())
    graph.append((c,a,b))

graph.sort()

parent = [i for i in range(V + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x]) 
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

total = 0

for i, j, k in graph:
    if find(j) != find(k):
        union(j, k)
        total += i

print(total)    
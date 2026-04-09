import sys
input = sys.stdin.readline

def DFS(G, V):
    visited = []
    stack = [V]
    while stack:
        Z = stack.pop()        
        if Z not in visited:
            visited.append(Z)
            if Z in G:
                for v in sorted(G[Z], reverse=True):
                    stack.append(v)
    return visited
    
def BFS(G, V):
    visited = []
    queue = [V]
    while queue:
        Z = queue.pop(0)
        if Z not in visited:
            visited.append(Z)
            if Z in G:
                for v in sorted(G[Z]):
                    queue.append(v)
    return visited

N, M, V = map(int,input().split())
G = {}

for _ in range(M):
    X, Y = map(int,input().split())
    if X in G:
        G[X].append(Y)
    else:
        G[X] = [Y]
    if Y in G:
        G[Y].append(X)
    else:
        G[Y] = [X]



dfs_result = DFS(G, V)
print(" ".join(map(str, dfs_result)))

bfs_result = BFS(G, V)
print(" ".join(map(str, bfs_result)))
    
import sys
input = sys.stdin.readline

N = int(input())
parents = list(map(int, input().split()))
D = int(input())

tree = [[] for _ in range(N)]
root_node = -1

for i in range(N):
    parent = parents[i]
    
    if parent == -1:
        root_node = i
    else:
        tree[parent].append(i)

count = 0

def DFS(node):
    global count

    is_leaf = True

    for child in  tree[node]:
        if child == D:
            continue
        is_leaf = False
        DFS(child)
    
    if is_leaf:
        count += 1

if D == root_node:
    print(0)
else:
    DFS(root_node)
    print(count)
import sys
input = sys.stdin.readline

def preorder(tree, root):
    if root == '.':
        return ""
    left = preorder(tree, tree[root][0])
    right = preorder(tree, tree[root][1])
    return root + left + right

def inorder(tree, root):
    if root == '.':
        return ""
    left = inorder(tree, tree[root][0])
    right = inorder(tree, tree[root][1])
    return left + root + right

def postorder(tree, root):
    if root == '.':
        return ""
    left = postorder(tree, tree[root][0])
    right = postorder(tree, tree[root][1])
    return left + right + root

N = int(input())
tree = {}

for _ in range(N):
    a, b, c = input().split()
    tree.setdefault(a, []).append(b)
    tree.setdefault(a, []).append(c)

string1 = ""
print(preorder(tree, 'A'))
print(inorder(tree, 'A'))
print(postorder(tree, 'A'))

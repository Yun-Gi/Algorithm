import sys
input = sys.stdin.readline

lst = list(input().split())
stack = []
for i in lst:
    if i == '+':
        A = stack.pop()
        B = stack.pop()
        stack.append(A+B)
    elif i == '-':
        A = stack.pop()
        B = stack.pop()
        stack.append(B-A)
    elif i == '*':
        A = stack.pop()
        B = stack.pop()
        stack.append(A*B)
    else:
        stack.append(int(i))

print(stack[0])
           





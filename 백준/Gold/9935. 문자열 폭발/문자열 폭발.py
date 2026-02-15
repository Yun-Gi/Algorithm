import sys
input = sys.stdin.readline

moonja = list(input().strip())
reze = list(input().strip())
reze_len = len(reze)

stack = []
anw = []

for char in moonja:
    stack.append(char)
    if len(stack) >= reze_len and stack[-reze_len:] == reze:
        del stack[-reze_len:]

result = ''.join(stack)
if result:
    print(result)
else:
    print("FRULA")
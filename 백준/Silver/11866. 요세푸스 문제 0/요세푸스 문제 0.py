N, K = map(int, input().split())

lst = [i + 1 for i in range(N)]
pointer = 0
result = []

while len(lst) > 0:
    pointer = (pointer + K - 1) % len(lst)
    result.append(lst.pop(pointer))

print("<", end="")
for i in range(N - 1):
    print(result[i], end=", ")
print(f"{result[N-1]}>")
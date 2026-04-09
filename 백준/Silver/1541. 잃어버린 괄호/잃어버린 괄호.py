import sys
input = sys.stdin.readline

sik = input().strip()

part = sik.split("-")
result = sum(map(int, part[0].split('+')))
part.pop(0)

for i in part:
    if '+' not in i:
        result -= int(i)
    else:
        X = i.split('+')
        Y = 0
        for j in X:
            Y += int(j)
        result -= Y

print(result)
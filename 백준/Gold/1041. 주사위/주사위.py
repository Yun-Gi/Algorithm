import sys
input = sys.stdin.readline

N = int(input())
dice = list(map(int, input().split()))
Rdice = []
Rdice.append(min(dice[0], dice[5]))
Rdice.append(min(dice[1], dice[4]))
Rdice.append(min(dice[2], dice[3]))
Rdice.sort()

d3 = Rdice[0] + Rdice[1] + Rdice[2]
d2 = Rdice[0] + Rdice[1]
d1 = Rdice[0]

anw = 4*d3 + (8*N-12) * d2 + ((N-2)**2 + 4*(N-1)*(N-2)) * d1

if N == 1:
    print(sum(dice) - max(dice))
else:
    print(anw)
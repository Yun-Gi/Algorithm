import sys

input = sys.stdin.readline

N = int(input())
dpl = [[0, 0, 0], [0, 0, 0]]
dps = [[0, 0, 0], [0, 0, 0]]

a, b, c = map(int, input().split())

dpl[0] = [a, b, c]
dps[0] = [a, b, c]

for _ in range(N-1):    
    a, b, c = map(int, input().split())

    dpl[1][0] = max(dpl[0][0], dpl[0][1]) + a
    dpl[1][1] = max(dpl[0][0], dpl[0][1], dpl[0][2]) + b
    dpl[1][2] = max(dpl[0][1], dpl[0][2]) + c
    dps[1][0] = min(dps[0][0], dps[0][1]) + a
    dps[1][1] = min(dps[0][0], dps[0][1], dps[0][2]) + b
    dps[1][2] = min(dps[0][1], dps[0][2]) + c
    dpl[0][0] = dpl[1][0]
    dpl[0][1] = dpl[1][1]
    dpl[0][2] = dpl[1][2]
    dps[0][0] = dps[1][0]
    dps[0][1] = dps[1][1]
    dps[0][2] = dps[1][2]

print(max(dpl[0]), min(dps[0]))
import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int,input().split())
id_pw = {}

for i in range(N):
    key, value = input().split()
    id_pw[key] = value

for i in range(M):
    id = input().strip()
    print(id_pw[id] + "\n")
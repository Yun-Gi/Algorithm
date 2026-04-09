import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

count = 0
i = 0

while i <= M - (2 * N + 1):
    if S[i] == 'I':
        match_length = 0
        while i + 1 < M and S[i + 1] == 'O' and i + 2 < M and S[i + 2] == 'I':
            match_length += 1
            i += 2
            if match_length == N:
                count += 1
                match_length -= 1
    i += 1

print(count)
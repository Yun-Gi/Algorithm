import sys
input = sys.stdin.readline
import math

N , M = map(int, input().split())
board = [input().strip() for _ in range(N)]
anw = -1

for r in range(N):         
    for c in range(M):       
        for dr in range(-N, N):
            for dc in range(-M, M):
                
                if dr == 0 and dc == 0:
                    continue
                
                step_r = r
                step_c = c
                num_str = ""
                
                while 0 <= step_r < N and 0 <= step_c < M:
                    num_str += board[step_r][step_c]
                    value = int(num_str)
                    if int(math.sqrt(value)) ** 2 == value:
                        if value > anw:
                            anw = value
                    if dr == 0 and dc == 0:
                        break
                    step_r += dr
                    step_c += dc

print(anw)
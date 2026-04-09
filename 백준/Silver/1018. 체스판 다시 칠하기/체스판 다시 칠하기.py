N, M = map(int,input().split())


result = 65
count0 = 0
count1 = 0

pattern_B = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]

pattern_W = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]

board = [input().strip() for _ in range(N)]

for i in range(N-7):
    for j in range(M-7):
        count0 = 0
        count1 = 0
        for k in range(8):
            for l in range(8):
                if board[i + k][j + l] != pattern_B[k][l]:
                    count0 += 1
                if board[i + k][j + l] != pattern_W[k][l]:
                    count1 += 1
        result = min(result, count0, count1)

print(result)

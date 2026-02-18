import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

visit = [False] * 26
move = ((1, 0), (-1, 0), (0, 1), (0, -1))
max_cnt = 0

def dfs(x, y, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            char_idx = ord(board[nx][ny]) - 65
            if visit[char_idx] == False:
                visit[char_idx] = True
                dfs(nx, ny, cnt + 1)
                visit[char_idx] = False

start_idx = ord(board[0][0]) - 65
visit[start_idx] = True
dfs(0, 0, 1)

print(max_cnt)
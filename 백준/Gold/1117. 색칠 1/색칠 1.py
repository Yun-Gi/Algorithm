import sys
input = sys.stdin.readline

W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

bound = min(f, W - f)

double_width = max(0, min(x2, bound) - x1)

single_width = (x2 - x1) - double_width

total_x_thickness = (double_width * 2) + single_width

painted_area = total_x_thickness * (y2 - y1) * (c + 1)

print(W * H - painted_area)
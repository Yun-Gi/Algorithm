import sys
input = sys.stdin.readline
import math

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    lens = y-x
    print(math.ceil(lens**0.5 * 2 - 1))
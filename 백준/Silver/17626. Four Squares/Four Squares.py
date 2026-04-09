import sys
import math
input = sys.stdin.readline

n = int(input().strip())

def is_square(k):
    return int(math.sqrt(k)) ** 2 == k

if is_square(n):
    sys.stdout.write('1\n')
else:
    result = 4
    for i in range(1, int(math.sqrt(n)) + 1):
        if is_square(n - i * i):
            result = min(result, 2)
        for j in range(1, int(math.sqrt(n - i * i)) + 1):
            if is_square(n - i * i - j * j):
                result = min(result, 3)
    sys.stdout.write(str(result) + '\n')
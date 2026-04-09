import math

A, B, V = map(int, input().split())

if A >= V:
    print(1)
else:
    days = (V - B - 1) // (A - B) + 1
    print(days)
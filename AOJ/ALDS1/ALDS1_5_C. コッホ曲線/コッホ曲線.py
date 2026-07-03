import sys
input = sys.stdin.readline
import math

def kohho(n, start, end):
    if n <= 0:
        return

    th = math.radians(60)
    s = ((2 * start[0] + end[0]) / 3.0, (2 * start[1] + end[1]) / 3.0)
    t = ((start[0] + 2 * end[0]) / 3.0, (start[1] + 2 * end[1]) / 3.0)
    u = ((t[0] - s[0]) * math.cos(th) - (t[1] - s[1]) * math.sin(th) + s[0], (t[0] - s[0]) * math.sin(th) + (t[1] - s[1]) * math.cos(th) + s[1])

    kohho(n-1, start, s)
    print(f"{s[0]:.8f} {s[1]:.8f}")
    kohho(n-1, s, u)
    print(f"{u[0]:.8f} {u[1]:.8f}")
    kohho(n-1, u, t)
    print(f"{t[0]:.8f} {t[1]:.8f}")
    kohho(n-1, t, end)

n = int(input())
print(f"{0.0:.8f} {0.0:.8f}")
kohho(n,(0.0,0.0),(100.0,0.0))
print(f"{100.0:.8f} {0.0:.8f}")


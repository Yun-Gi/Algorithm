import sys

def custom_round(number):
    if number - int(number) >= 0.5:
        return int(number) + 1
    else:
        return int(number)

N = int(sys.stdin.readline().strip())
level = []

for i in range(N):
    level.append(int(sys.stdin.readline().strip()))

level.sort()
cut = custom_round(N * 0.15)

subset = level[cut:N - cut]
total_sum = sum(subset)


if N == 0:
    average = 0
else:
    average = total_sum / len(subset)
average = custom_round(average)

print(average)
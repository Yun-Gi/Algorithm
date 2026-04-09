N = int(input())

result = 0



for i in range(N // 3 + 1):
    if (N - 3 * i) % 5 == 0:
        result = i + (N - 3 * i) // 5
        print(result)
        break
if result == 0:
    print(-1)
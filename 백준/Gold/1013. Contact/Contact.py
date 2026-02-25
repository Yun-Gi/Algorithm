import sys
input = sys.stdin.readline

def sol(l):
    pointer = 0
    while pointer < len(l):
        if l[pointer] == '0':
            if pointer + 1 < len(l) and l[pointer + 1] == '1':
                pointer += 2
            else:
                return 'NO'
        
        elif l[pointer] == '1':
            if pointer + 2 < len(l) and l[pointer + 1] == '0' and l[pointer + 2] == "0":
                pointer += 3
            else:
                return 'NO'
            while pointer < len(l) and l[pointer] == '0':
                pointer += 1

            if pointer == len(l):
                return 'NO'
            
            pointer += 1

            while pointer < len(l) and l[pointer] == '1':
                if pointer + 2 < len(l) and l[pointer + 1] == '0' and l[pointer + 2] == '0':
                    break
                pointer += 1
    return 'YES'

T = int(input())

for _ in range(T):
    moon = input().strip()
    print(sol(moon))
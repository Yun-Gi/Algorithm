import sys
input = sys.stdin.readline

N = int(input())
crain = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

crain.sort(reverse=True)
box.sort(reverse=True)

if box[0] > crain[0]:
    print(-1)
else:
    time = 0

    while box:
        for i in crain:
            for b in box:
                if b <= i:
                    box.remove(b)
                    break
                    
        time += 1
        
    print(time)
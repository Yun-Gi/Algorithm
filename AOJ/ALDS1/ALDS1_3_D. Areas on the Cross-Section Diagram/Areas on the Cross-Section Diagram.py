import sys
input = sys.stdin.readline

land = input()
A = 0
tamari = []
lst = []

for i in range(len(land)):
    if land[i] == "\\":
        lst.append(i)
    elif land[i] =='/' and lst:
        x = lst.pop()
        current_area = i - x
        A += current_area
        while tamari and tamari[-1][0] > x:
            _ , prev_area = tamari.pop()
            current_area += prev_area    
            
        tamari.append((x, current_area))


print(A)
areas = [i[1] for i in tamari]
print(len(areas), *areas)











           





N = int(input())
pointer = 0

lst = []

for i in range(N):
    lst.append(i+1)

while len(lst) != pointer+1:
    pointer += 1
    num = lst[pointer]
    lst.append(num)
    pointer += 1
    

print(lst[pointer])
n = int(input())
list = []

while n != -1:
    for i in range(1,n):
        if n % i == 0:
            list.append(i)
    
    if sum(list) == n:
        print(f"{n} =",end=" ")
        for i in list:
            if i == list[len(list)-1]:
                print(f"{i}")
            else:
                print(f"{i}",end=" + ")

    else:
        print(f"{n} is NOT perfect.")

    n = int(input())
    list = []

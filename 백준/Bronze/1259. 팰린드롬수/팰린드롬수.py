l = input().strip() 

while l != '0':
    rl = l[::-1]
    if l == rl:
        print("yes")
    else:
        print("no")
    l = input().strip() 
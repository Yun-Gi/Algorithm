import sys
input = sys.stdin.readline

def is_prime(x):
    if x < 2:
        return False    
    elif x == 2:
        return True      
    if x % 2 == 0:
        return False    
    i = 3
    while i * i <= x:    
        if x % i == 0:
            return False  
        i += 2
    return True   
        
n = int(input())
count = 0
for _ in range(n):
   i = int(input())
   if is_prime(i):
      count += 1

print(count)

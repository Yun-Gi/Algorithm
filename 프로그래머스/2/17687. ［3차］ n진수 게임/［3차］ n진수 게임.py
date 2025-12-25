def solution(n, t, m, p):
    answer = ''
    full_string = ''
    num = 0
    while len(full_string) < t * m:
        full_string += convert(num, n)
        num += 1
    
    answer = full_string[p-1::m][:t]
        
    return answer

                
def convert(num, base):
    if num == 0: return "0"
    
    digits = "0123456789ABCDEF"
    result = ""
    
    while num > 0:
        num, remainder = divmod(num, base) 
        result += digits[remainder]

    return result[::-1]
        
            
        
        
        
 
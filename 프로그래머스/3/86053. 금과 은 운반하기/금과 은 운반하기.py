def solution(a, b, g, s, w, t):
    answer = -1

    start = 0
    end = 10**15 
    answer = end 
    
    cityCount = len(g)

    while start <= end:
        mid = (start + end) // 2  
        
        cumulative_gold = 0
        cumulative_silver = 0
        all_cumulative = 0
        
        for i in range(cityCount):
            move_cnt = mid // (t[i] * 2)
            
            if mid % (t[i] * 2) >= t[i]:
                move_cnt += 1
                
            max_weight = move_cnt * w[i]
            
            cumulative_gold += min(g[i], max_weight)
            cumulative_silver += min(s[i], max_weight)
            all_cumulative += min(g[i] + s[i], max_weight)

        if cumulative_gold >= a and cumulative_silver >= b and all_cumulative >= a + b:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return answer
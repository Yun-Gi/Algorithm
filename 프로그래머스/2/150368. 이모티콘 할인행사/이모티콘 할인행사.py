from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    rates = [10, 20, 30, 40]
    
    for discounts in product(rates, repeat=len(emoticons)):
        prices = []
        for i in range(len(emoticons)):
            price = emoticons[i] * (100 - discounts[i]) // 100 
            prices.append(price)
            
        total_plus = 0 
        total_sales = 0 

        for user_rate, user_limit in users:
            buy_sum = 0 

            for discount, price in zip(discounts, prices):
                if discount >= user_rate:
                    buy_sum += price      
            
            if buy_sum >= user_limit:
                total_plus += 1  
            else:
                total_sales += buy_sum
        
        if answer < [total_plus, total_sales]:
            answer = [total_plus, total_sales]
            
    return answer


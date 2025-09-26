def maxprofit(prices):
    min_price=prices[0]
    max_profit=0
    
    for i in range(1,len(prices)):
        if prices[i]< min_price:
            min_price=prices[i]
        
        max_profit=max(max_profit,prices[i]-min_price)
    
    return max_profit

prices=list(map(int, input("Enter the prices:").split()))
print("The maximum profit is:",maxprofit(prices))
def buyAndSell(prices):
    n=len(prices)
    buy=prices[0]
    profit=0
    max_profit=0
    left,right=0,0

    for i in range(1,n):
        if buy>prices[i]:
            buy=prices[i]
            left=i
        else:
            profit=prices[i]-buy
            if profit>max_profit:
                max_profit=profit
                right=i
            profit=0
    
    return left,right

prices = [7,2,1,5,3,6,4]
print(buyAndSell(prices))


def maxProfit(prices):
    n=len(prices)
    buy=0
    current_profit=0
    profit=0

    for i in range(1,n):
        if prices[i]<prices[buy]:
            buy=i
        else:
            current_profit=prices[i]-prices[buy]
            if current_profit>profit:
                profit=current_profit
    return profit
    

prices = [7,1,5,3,6,4]
# prices = [2,1,2,1,0,1,2]
a=maxProfit(prices)
print(a)

# for i in range(n):
#         if prices[i]<prices[i+1]:
#             if prices[i]<prices[buy]:
#                 buy=i
#             current_profit=prices[i+1]-prices[buy]
#             if current_profit>profit:
#                 profit=current_profit
#     return profit
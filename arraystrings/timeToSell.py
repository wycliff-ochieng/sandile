def maxProfit(prices:list[int])->int:
    max_profit=float('inf')

    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            profit=prices[i]-prices[i]

            if profit>0:
                max_profit = max(profit,max_profit)

        return max_profit
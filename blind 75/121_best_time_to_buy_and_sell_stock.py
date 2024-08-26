def maxProfit(prices: list[int]) -> int:
    l_ptn, r_ptn = 0, 1
    mx_profit = 0

    while r_ptn < len(prices):
        if prices[l_ptn] < prices[r_ptn]:
            profit = prices[r_ptn] - prices[l_ptn]
            mx_profit = max(mx_profit, profit)
        else:
            l_ptn = r_ptn
        r_ptn += 1
    return mx_profit

result = maxProfit([7,2,5,3,6,4,1,9])
print(result)
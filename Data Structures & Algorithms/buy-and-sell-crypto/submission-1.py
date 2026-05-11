class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Bounds are indices between which stock will be bought & sold
        # Initialized at 0,0 since nothing has happened yet
        # Current bound is the next best runner-up to see if something
        # is better
        best_bound = (0,0)
        current_bound = (0,None)
        for i in range(len(prices)):
            if prices[i] < prices[current_bound[0]]:
                current_bound = (i, None)
                continue
            if current_bound[1] == None or prices[i] > prices[current_bound[1]]:
                current_bound = (current_bound[0], i)
                best_profit = prices[best_bound[1]] - prices[best_bound[0]]
                current_profit = prices[current_bound[1]] - prices[current_bound[0]]
                if current_profit > best_profit:
                    best_bound = current_bound
        return prices[best_bound[1]] - prices[best_bound[0]]
            
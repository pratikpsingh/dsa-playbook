class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) in {0, 1}:
            return 0

        max_value = prices[-1]
        max_profit = 0
        i = len(prices) - 2 # Start from second last index
        while i>= 0:
            profit = max_value - prices[i]

            if max_profit < profit:
                max_profit = profit

            if max_value < prices[i]:
                max_value = prices[i]

            i -= 1

        return max_profit

        
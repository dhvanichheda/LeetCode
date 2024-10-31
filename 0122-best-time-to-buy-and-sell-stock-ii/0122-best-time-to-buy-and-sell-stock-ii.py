class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0 

        for idx in range(1, len(prices)):
            prev_day_profit = max(0, prices[idx] - prices[idx-1])

            if prices[idx] > min_price:
                prev_min_profit = prices[idx] - min_price
            else:
                prev_min_profit = 0
                min_price = prices[idx]

            max_profit = max(max_profit + prev_day_profit, prev_min_profit)

        return max_profit
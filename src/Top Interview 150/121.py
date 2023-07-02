class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

solution = Solution()
prices = [7, 1, 5, 3, 6, 4]
result = solution.maxProfit(prices)
print(result)  # Output: 5

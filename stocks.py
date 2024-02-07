class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        # Initialize variables
        buy_price = prices[0]
        max_profit = 0

        # Iterate through the prices
        for price in prices[1:]:
            # Update the minimum price
            buy_price = min(buy_price, price)

            # Update the maximum profit
            max_profit = max(max_profit, price - buy_price)

        return max_profit
solution = Solution()
x= solution.maxProfit([6,1,2,4,5])
print(x)

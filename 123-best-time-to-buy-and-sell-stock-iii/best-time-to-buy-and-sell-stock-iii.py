class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        
        # Initialize two 2D arrays, ahead and cur, both of size 2x3, with 0 values
        ahead = [[0 for _ in range(3)] for _ in range(2)]
        cur = [[0 for _ in range(3)] for _ in range(2)]

        for ind in reversed(range(n)):
            for buy in range(2):         # Loop for buy (0) and sell (1) states
                for trans in range(1, 3):  # Loop for transaction counts (1 and 2)
                    if buy == 0:  # Buying state
                        cur[buy][trans] = max(-prices[ind] + ahead[1][trans], 0 + ahead[0][trans])
                    else:  # Selling state
                        cur[buy][trans] = max(prices[ind] + ahead[0][trans - 1], 0 + ahead[1][trans])

            # Update ahead for the next iteration
            ahead = [row[:] for row in cur]  # Deep copy cur into ahead to avoid reference issues

        return ahead[0][2]
class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int: 
        
        m = len(coins)
        
        n = len(coins[0])
        
        def isValid(row,col):
            
            return 0 <= row < m  and 0 <= col < n
        
        dp = [[[-float('inf') for chances in range(2+1)]for col in range(n+1)] for row in range(m+1)]   

        dp[m-1][n-1][0] = coins[m-1][n-1]

        dp[m-1][n-1][1] = dp[m-1][n-1][2] = 0

        for row in reversed(range(m)):

            for col in reversed(range(n)):

                if row == m - 1 and col == n-1 :

                        continue

                for chances in range(3):

                    ans = - float('inf')

                    if coins[row][col] >= 0:

                    # get right money if possible

                        if isValid(row,col+1):

                            rightMoney = coins[row][col] + dp[row][col+1][chances]

                            ans = max(ans,rightMoney)

                        # get down money if possible

                        if isValid(row+1,col):

                            downMoney = coins[row][col] + dp[row+1][col][chances]

                            ans = max(ans,downMoney)
                        
                        dp[row][col][chances] = ans
                    
                    elif coins[row][col] < 0 :

                        if chances:
                            
                            # get right money if possible

                            if isValid(row,col+1):

                                rightMoney = 0 + dp[row][col+1][chances-1]

                                ans = max(ans,rightMoney)

                            # get down money if possible

                            if isValid(row+1,col):

                                downMoney = 0 + dp[row+1][col][chances-1] 

                                ans = max(ans,downMoney)

                        # get right money if possible

                        if isValid(row,col+1):

                            rightMoney = coins[row][col] + dp[row][col+1][chances]

                            ans = max(ans,rightMoney)

                        # get down money if possible

                        if isValid(row+1,col):

                            downMoney = coins[row][col] + dp[row+1][col][chances]  

                            ans = max(ans,downMoney)
                        
                        dp[row][col][chances] = ans

        return max(dp[0][0])

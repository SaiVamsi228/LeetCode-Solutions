class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)

        dp = [[False for bal in range(n+1)] for i in range(n+1)]

        balance = 0

        dp[n][balance] = True 

        for i in reversed(range(n)):

            for balance in range(n):

                if i == n and balance == 0:

                    continue

                if s[i] == "(":

                    if balance + 1 <= n :

                        dp[i][balance] = dp[i+1][balance + 1]
                
                elif s[i] == ")":

                    if balance - 1 >= 0 :

                        dp[i][balance] = dp[i+1][balance - 1]

                elif s[i] == "*":

                    bal_plus_one = dp[i+1][balance + 1] 
                    
                    bal_minus_one = dp[i+1][balance - 1] 

                    only_bal = dp[i+1][balance] 
                    
                    dp[i][balance] =  only_bal or bal_plus_one or bal_minus_one
        

        return dp[0][0]
                    

                

                

                



        return isPossible(0,0)
            

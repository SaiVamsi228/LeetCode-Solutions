class Solution:
    def checkValidString(self, s: str) -> bool:
        
        def isPossible(i,balance):

            if i == n :

                if balance == 0:

                    return True
                
                return False
            
            if balance < 0 :

                return False
            
            if (i,balance) in dp:
                
                return dp[(i,balance)]

            char = s[i]

            if char == "(":

                dp[(i,balance)] = isPossible(i+1,balance + 1)

                return dp[(i,balance)]
            
            elif char == ")":

                dp[(i,balance)] = isPossible(i+1,balance-1)

                return dp[(i,balance)]
            
            elif char == "*":

                dp[(i,balance)] = isPossible(i+1,balance) or isPossible(i+1,balance+1) or isPossible(i+1,balance - 1)

                return dp[(i,balance)] 
            
        
        n = len(s)

        dp = {}

        return isPossible(0,0)
            

class Solution:
    def climbStairs(self, n: int) -> int:

        if n==1:

            currentStepWays = 1
        
        if n==2 : 

            currentStepWays = 2

        firstStepWays = 1

        if n>=2:
            
            secondStepWays = 2

        for i in range(3,n+1):

            currentStepWays = secondStepWays + firstStepWays

            firstStepWays = secondStepWays

            secondStepWays = currentStepWays
        
        return currentStepWays
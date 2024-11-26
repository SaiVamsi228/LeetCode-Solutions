class Solution:
    def isSubsetSum (self, arr, target):
        # code here 
        
        n = len(arr)
        
        dp = [ [False for j in range(target + 1)] for i in range(n+1)]
        
        for j in range(target + 1): # if no ele exists
            
            dp[0][j] = False
            
        for i in range(n+1): # target 0 can definetely be made
            
            dp[i][0] = True
        
        for i in range(1,n+1):
            
            for j in range(1, target + 1):
                
                if arr[i-1] <= j:
                    
                    dp[i][j] = dp[i-1][j - arr[i-1]] or dp[i-1][j]
                
                elif arr[i-1] > j:
                    
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][target]

    def canPartition(self, nums: List[int]) -> bool:
        
        nums_sum = sum(nums)

        if nums_sum % 2 == 1:

            return False
        
        target  = nums_sum // 2

        return self.isSubsetSum(nums, target)
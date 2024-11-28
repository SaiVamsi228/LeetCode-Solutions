class Solution:
    def rob(self, nums: List[int]) -> int:
        def getMaxRobbery(nums):

            n = len(nums)

            dp = [0 for i in range(n+1)]

            dp[1] = nums[0]

            if n == 1:

                return dp[1]

            dp[2] = max(nums[0], nums[1])

            if n == 2:

                return dp[2]

            for i in range(3,n+1):

                dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])

            return dp[n]
        
        n = len(nums)

        if n == 1:

            return nums[0]
        # because we cant rob simulataneously
        
        return max(getMaxRobbery(nums[:-1]), getMaxRobbery(nums[1:]))
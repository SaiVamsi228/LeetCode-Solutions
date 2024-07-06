class Solution:

    def maxLoot(self,nums):

        n = len(nums)

        dp = [ -1 for i in range(n+1)]

        dp[1] = nums[0]

        if n == 1:

            return dp[1]
            
        dp[2] = max(nums[0], nums[1])

        for i in range(3,n+1):

            dp[i] = max(nums[i-1] + dp[(i-2)%n], dp[(i-1)%n])
        
        return dp[n]


    def rob(self, nums: list[int]) -> int:
        
        # As the first and the last houses are connected we cant
        # loot both houses. As our function knows to allow looting
        # in both the houses, we send first array of houses which
        # contains first and not last and last and not first.
        # Reason being : Both houses can't be looted as they are adjacent.

        if len(nums) == 1:

            return nums[0]

        return max(self.maxLoot(nums[1:]), self.maxLoot(nums[:-1]))



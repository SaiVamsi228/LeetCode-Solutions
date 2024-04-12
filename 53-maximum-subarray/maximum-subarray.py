class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Kadane's Algorithm
        
        n = len(nums)

        sum_ = 0

        maxi = nums[0]

        for i in range(n):

            if sum_ < 0 :

                sum_ = 0

                sum_ += nums[i]
            
            else:

                sum_ += nums[i]
            
            maxi = max(sum_,maxi)
        
        return maxi
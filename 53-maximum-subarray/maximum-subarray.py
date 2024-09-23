class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        mx = nums[0]

        cS = nums[0]


        n = len(nums)

        for i in range(1,n):

            num = nums[i]

            if cS < 0:

                cS = num
            
            else:

                cS += num

            mx = max(cS, mx)
        
        return mx



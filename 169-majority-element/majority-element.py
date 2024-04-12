class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)

        hm = {}

        for i in range(n):

            if nums[i] not in hm:

                hm[nums[i]] = 1
            
            else:

                hm[nums[i]] += 1
            
            if hm[nums[i]] > n//2:

                return nums[i]
        


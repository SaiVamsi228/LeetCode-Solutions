class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(0,n,2):

            if i + 1 < n and nums[i] != nums[i+1]:

                return nums[i]
        
        return nums[-1]
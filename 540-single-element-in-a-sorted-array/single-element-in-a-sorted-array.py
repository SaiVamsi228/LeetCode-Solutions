class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)

        for ind in range(1,n,2):

            if nums[ind] != nums[ind - 1]:

                return nums[ind - 1]
            
        # if the index goes out of bound then the last ele is repeated once
        return nums[-1]



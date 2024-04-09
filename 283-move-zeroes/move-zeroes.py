class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        j = 0 

        for i in range(n):

            if nums[i] == 0:

                # Telling j to get valid non_zero_element_ind
                j  = i + 1

                while j < n and nums[j]==0:

                    j+=1

                if j>=n:
                    break # Already zeroes are at the end
                else:
                    nums[i],nums[j] = nums[j], nums[i]
            
        return nums
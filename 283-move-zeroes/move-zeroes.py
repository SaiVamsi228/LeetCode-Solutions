class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n= len(nums)

        non_zero_arr = [0] * n

        k=0

        for i in range(n):

            if nums[i] != 0:

                non_zero_arr[k] = nums[i]

                k += 1
        
        nums[:] = non_zero_arr

        return nums
        




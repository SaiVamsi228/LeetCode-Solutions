class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)

        low, mid = 0, 0

        high = n - 1

        while mid <= high:

            if nums[mid] == 0:

                nums[low], nums[mid] = nums[mid], nums[low]

                low += 1

                mid += 1
            
            elif nums[mid] == 1:

                mid += 1
            
            elif nums[mid] == 2:

                nums[mid], nums[high] = nums[high], nums[mid]

                high -= 1
        
        return nums
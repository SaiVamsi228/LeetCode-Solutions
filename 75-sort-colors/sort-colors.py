class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        count_0, count_1, count_2 = 0, 0, 0

        for num in nums:

            if num == 0:

                count_0 += 1
            
            if num == 1:

                count_1 += 1
            
            if num == 2:

                count_2 += 1
        
        for i in range(n):

            if count_0:

                nums[i] = 0

                count_0 -= 1
            
            elif count_1 :

                nums[i] = 1

                count_1 -= 1
            
            else:

                nums[i] = 2

                count_2 -= 1
        
        return nums




        
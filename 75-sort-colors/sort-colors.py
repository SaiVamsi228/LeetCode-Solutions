class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red_cnt = 0

        white_cnt = 0

        blue_cnt = 0

        for num in nums:

            if num == 0: red_cnt += 1

            elif num == 1 : white_cnt += 1

            else: blue_cnt += 1
        
        n = len(nums)

        for i in range(n):

            if red_cnt :

                nums[i] = 0

                red_cnt -= 1
            
            elif white_cnt :

                nums[i] = 1

                white_cnt -= 1
            
            else:

                nums[i] = 2

                blue_cnt -= 1
        
        return nums
        
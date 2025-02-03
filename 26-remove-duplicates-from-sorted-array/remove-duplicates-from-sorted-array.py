class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        uniq_ptr = 0

        n = len(nums)

        if n == 1:

            return 1

        for i in range(1,n):

            if nums[i] != nums[i-1]:

                uniq_ptr += 1

                nums[uniq_ptr] = nums[i]


        return uniq_ptr + 1

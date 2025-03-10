class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        dist_ptr = 0

        n = len(nums)

        for i in range(1,n):

            if nums[i] == nums[dist_ptr]:

                continue
            
            else:

                dist_ptr += 1

                nums[dist_ptr] = nums[i]
        
        return dist_ptr + 1
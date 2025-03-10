class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        prev = nums[0]

        dist_ptr = 0

        n = len(nums)

        for i in range(1,n):

            if nums[i] == prev:

                continue
            
            else:

                dist_ptr += 1

                nums[dist_ptr] = nums[i]

                prev = nums[dist_ptr]
        
        return dist_ptr + 1
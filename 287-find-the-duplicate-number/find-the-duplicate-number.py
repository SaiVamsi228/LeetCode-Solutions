class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n):

            cur_num = abs(nums[i])

            if nums[cur_num - 1 ] < 0 :

                return cur_num
            
            else:

                nums[cur_num - 1] = -1 * nums[cur_num - 1]
        
        return -1
    
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        mx = 0

        cur_cnt = 0

        n = len(nums)

        for i in range(n):

            if nums[i] == 1:

                cur_cnt += 1
            
            else:

                cur_cnt = 0
            
            mx = max(cur_cnt , mx)
        
        return mx
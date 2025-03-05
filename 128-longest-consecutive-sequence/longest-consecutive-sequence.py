class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums :

            return 0
            
        nums.sort()

        mx = 1

        cur_seq_len = 1

        n = len(nums)

        for i in range(1,n):

            if nums[i] == nums[i-1]:

                continue

            if nums[i] == nums[i-1] + 1 :

                cur_seq_len += 1
            
            else:

                cur_seq_len = 1
            
            mx = max(mx,cur_seq_len)

        return mx

            
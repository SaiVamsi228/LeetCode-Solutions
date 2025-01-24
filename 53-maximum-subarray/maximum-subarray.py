class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur_sub_arr_sum = nums[0]

        mx_sub_arr_sum = nums[0]

        n = len(nums)

        for i in range(1,n):

            if cur_sub_arr_sum < 0 :

                cur_sub_arr_sum = 0
            
            cur_sub_arr_sum += nums[i]

            mx_sub_arr_sum = max(mx_sub_arr_sum, cur_sub_arr_sum)
        
        return mx_sub_arr_sum
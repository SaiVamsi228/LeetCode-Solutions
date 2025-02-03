class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_cnt = 0

        i = j = 0

        n = len(nums)

        mx = 0

        while j < n  :

            if nums[j] == 0:

                zero_cnt += 1
            
            if zero_cnt > k :

                while i <= j and zero_cnt > k :
                    
                    if nums[i] == 0:

                        zero_cnt -= 1

                    i += 1
                
            if zero_cnt <= k:

                mx = max(j-i+1,mx)
            
            j += 1
        
        return mx

                


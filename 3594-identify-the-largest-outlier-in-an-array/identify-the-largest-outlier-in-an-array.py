from collections import Counter
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        
        tot_sum = sum(nums)
        
        maxi = min(nums)
        
        cnt = Counter(nums)
        
        for out in nums:
            
            special_sum_2 = tot_sum - out
            
            if special_sum_2 % 2 == 1:
                
                continue
            
            sm = special_sum_2 // 2
            
            
            # print(tot_sum, special_sum_2, sm, out)
            
            if sm == out :
                
                if cnt[out]  >= 2:
                    
                    maxi = max(out, maxi)
            
            else:
                
                if sm in cnt and cnt[out] >= 1:

                    maxi = max(out, maxi)
        
        return maxi
                
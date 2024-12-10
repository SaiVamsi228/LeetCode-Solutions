from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        res = [nums[0]]
        
        n = len(nums)
        
        for i in range(1,n):
            
            num = nums[i]
            
            if res == [] or res[-1] < num:
                
                res.append(num)
            
            else:
                
                getPos = bisect_left(res,num)
        
                res[getPos] = num
        
        return len(res)
from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def getMaxMoney(ind,first_house_robbed):

            if ind >= n :

                return 0 
            
            if ind == n - 1 and first_house_robbed:

                return 0
            
            if ind == 0:

                rob_money = nums[ind] + getMaxMoney(ind+2,1)
            
            else:
                
                rob_money = nums[ind] + getMaxMoney(ind+2,first_house_robbed)
            
            rob_others = getMaxMoney(ind+1,first_house_robbed)

            return max(rob_money,rob_others)
        
        n = len(nums)

        return getMaxMoney(0,0)


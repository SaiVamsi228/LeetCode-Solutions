class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        mc, c = 0 , 0

        for num in nums:

            if num== 1:

                c+= 1

                mc = max(mc,c)
            
            else:
                c = 0
        
        return mc


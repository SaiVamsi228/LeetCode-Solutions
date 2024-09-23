class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        mx = 0

        cC = 0

        for num in nums:

            if num == 1:

                cC += 1
            
                mx = max(mx, cC)
            
            else:

                cC = 0


        
        return mx
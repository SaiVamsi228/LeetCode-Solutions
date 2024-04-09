class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        bucket = [0 for i in range(n)]

        for num in nums:

            if num < n:
                
                bucket[num] = 1
        
        for i in range(n):

            if bucket[i] == 0:

                return i
        
        return i+1

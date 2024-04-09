class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        result = 0

        for i in range(n):

            result ^= i

            result ^= nums[i]

        result ^= n
        
        return result
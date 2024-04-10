class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        result= 0

        for num in nums:

            result^= num
        
        return result
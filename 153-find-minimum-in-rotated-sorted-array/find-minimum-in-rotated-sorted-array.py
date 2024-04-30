class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)

        mini = 2**31 + 1
        
        for num in nums:

            mini = min(num,mini)

        return mini
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        insertPos = n

        for i in range(n):

            if nums[i] >= target:

                insertPos = i

                break
        
        return insertPos
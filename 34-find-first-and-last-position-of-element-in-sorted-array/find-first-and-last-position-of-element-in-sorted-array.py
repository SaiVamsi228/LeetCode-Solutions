class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = -1

        right = -1

        n = len(nums)

        for i in range(n):

            if nums[i] == target :

                if left == -1:

                    left = right = i
                
                if i < left :

                    left = i
                
                if i > right :

                    right = i
        
        return [left,right]


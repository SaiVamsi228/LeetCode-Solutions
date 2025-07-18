class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)

        left = 0
        
        right = n - 1

        mn = float('inf')

        while left <= right:

            mid = (left + right)//2

            if nums[left] <= nums[mid]:
                # left is sorted

                mn = min(mn,nums[left])

                left = mid + 1
            
            else:
                # right is sorted
                mn = min(mn,nums[mid])

                right = mid - 1
        
        return mn
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)

        low, high = 0, n-1

        mini = 2**31 + 1

        while low <= high :

            mid = (low + high)//2

            if nums[mid] < mini :

                mini = nums[mid]

            if nums[low] <= nums[mid]:

                mini = min(nums[low],mini)

                low = mid+1
            
            else:

                high = mid - 1
        
        return mini
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1 :

            return 0
        
        if nums[0] > nums[1]:

            return 0
        
        if nums[n-1] > nums[n-2]:

            return n-1

        left , right = 1, n - 2

        while left <= right:

            mid = (left + right)//2

            if nums[mid-1] < nums[mid] > nums[mid+1]:

                return mid
            
            if nums[mid - 1] < nums[mid] :

                left = mid + 1
            
            else:

                right = mid - 1

                
            

            

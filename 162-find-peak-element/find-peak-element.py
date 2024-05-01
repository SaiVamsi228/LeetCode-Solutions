class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # Note: We need to return ANY peak

        n = len(nums)

        if n==0:
            return 0
        
        if n == 1:
 
            return 0 # If only 1 ele exists 0th ele is the peak
        
        if nums[n-1] > nums[n-2]:

            return n-1 # Checking last two as it cannot be checked 
                        # for mid + 1 if mid lies on n-1
        
        if nums[0] > nums[1] :

            return 0    # Checking first two as it cannot be checked 
                        # for mid - 1 if mid lies on 0
        
        low, high = 1, n-2  # Checking leaving the edge cases

        while low <= high :

            mid = (low + high) // 2

            # If my current mid is peak return it

            if  nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:

                return mid

            # If my mid is greater than the previous then my peak
            #  will be to the right as we are expecting a definite 
            # ascending order as we have already looked for the 
            # first and last elements
            
            if nums[mid] > nums[mid-1] :

                low = mid + 1
            
            # If my mid is greater than the next or not greater than 
            # previous or next then my peak will be to the left

            else:

                high = mid - 1
                



        
        
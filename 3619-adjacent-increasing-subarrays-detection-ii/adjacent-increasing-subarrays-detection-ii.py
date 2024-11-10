class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        
        i = 0
        j = 1

        n = len(nums)

        curr = prev = 0

        maxi = 1

        while j < n:

            while j < n and nums[j] > nums[j-1]:

                j += 1

            curr = j - i
            
            maxi = max(maxi, curr//2, min(curr, prev))

            prev = curr 

            curr = 0

            i = j

            j += 1

    
        return maxi

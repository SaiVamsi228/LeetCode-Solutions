class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = list(set(nums))

        nums = sorted(nums)

        n = len(nums)

        if n == 1 or n == 0:

            return n

        i = 0

        j = 1

        mx = 1

        while j < n :

            if nums[j] == nums[j-1] + 1 :

                mx = max(mx,j-i+1)
            
            else:

                i = j
            
            j += 1
        
        return mx
            
            

            

        
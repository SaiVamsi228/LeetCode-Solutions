class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
      
        n = len(nums)  # Size of the array

        if n == 1:

            return nums[0]

        for i in range(n):

            if i==0 :

                if nums[i] != nums[i+1]:

                    return nums[i]
            

            if i == n-1:

                if nums[i] != nums[i-1]:

                    return nums[i]
            
            if nums[i] != nums[i+1] and nums[i] != nums[i-1]:

                return nums[i]
        

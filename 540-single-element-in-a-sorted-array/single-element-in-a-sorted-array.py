class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)

        left , right = 0 , n - 1

        while left <= right:

            mid = (left + right)//2

            if mid % 2 == 0:

                # Even Ind
                # if it is pairing with right ele if exists then something is wrong in right
                # else something is wrong is left

                if mid + 1 > n - 1 :

                    return nums[mid]
                
                elif nums[mid] == nums[mid + 1]:

                    left = mid + 1
                
                else:

                    right = mid - 1
            
            else:

                # Odd Ind
                # if it is pairing with left ele if exists then something is wrong in right
                # else something is wrong is left

                if mid - 1 < 0 :

                    return nums[mid]
                
                if nums[mid] == nums[mid- 1]:

                    left = mid + 1
                
                else:

                    right = mid - 1
            
        
        return nums[left]

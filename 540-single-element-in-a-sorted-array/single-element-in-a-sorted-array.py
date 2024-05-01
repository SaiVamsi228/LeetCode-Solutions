class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)

        low, high = 0, n-1

        while low <= high :

            mid = (low+high)//2

            if mid%2 == 0:

                if mid-1 >=0 :

                    if nums[mid-1] != nums[mid]: # if there is not no problem in the left then move right

                        low = mid + 1
                    
                    else: #else move left

                        high = mid - 1
                        
                else:

                    return  nums[mid]

            
            else:

                if mid-1 >= 0 :
                    
                    if nums[mid-1] == nums[mid]: # if there is not no problem in the left then move right

                        low = mid + 1
                    
                    else: #else move left

                        high = mid - 1
                
                else:

                    return nums[mid]

        if mid%2 == 1:

            return nums[mid-1]

        return nums[mid]


            


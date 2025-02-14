class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)

        low , high = 0, n - 1

        if n == 1 :

            return nums[0]


        while low <= high :

            mid = (low + high)//2

            if mid == n - 1:

                return nums[mid]

            if mid % 2 == 0 :

                if nums[mid] == nums[mid + 1] :

                    low = mid + 1
                
                else:

                    high = mid - 1
            
            else:

                if nums[mid] != nums[mid+1]:

                    low = mid + 1
                
                else:

                    high = mid - 1
        
        if low == n :

            return nums[n-1]
            
        return nums[low] 
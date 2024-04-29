class Solution:

    def getLeft(self,nums,target):

        n = len(nums)

        low, high = 0, n-1

        left = -1

        while low <= high:

            mid = (low+high)//2

            
            if nums[mid] >= target:

                if nums[mid] == target:

                    if left == -1:

                        left = mid
                    
                    if mid < left :

                        left = mid
                
                high = mid - 1
                
            else:

                low = mid + 1
        
        return left

    def getRight(self,nums,target):

        n = len(nums)

        low, high = 0, n-1

        right = -1

        while low <= high:

            mid = (low+high)//2

            if nums[mid] <= target:

                if nums[mid] == target:

                    if right == -1:

                        right = mid
                    
                    if mid > right :

                        right = mid

                    
                low = mid + 1
                
            else:

                high = mid - 1
        
        return right

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        left = self.getLeft(nums,target)

        right = self.getRight(nums,target)

        return [left,right]
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)

        low, high = 0, n - 1

        while low <= high:

            mid = (low + high)//2

            print(low,high,mid)

            if mid % 2 == 0:

                if mid + 1 >= n :

                    return nums[mid]
                
                curr, nxt = nums[mid], nums[mid + 1]

                if curr == nxt:

                    # our ans lies on right

                    low = mid + 1

                else:

                    high = mid - 1 
            
            elif mid % 2 == 1:

                curr, prev = nums[mid], nums[mid - 1]

                if curr == prev:

                    low = mid + 1
                
                else:

                    high = mid - 1
        

        return nums[low]
            
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def getFO(arr):
            n = len(arr)
            left = 0
            right = n - 1
            ans = -1
            while left <= right:
                mid = (left + right)//2
                if arr[mid] == target:
                    ans = mid
                    right = mid - 1
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return ans
        
        def getLO(arr):
            n = len(arr)
            left = 0
            right = n - 1
            ans = -1
            while left <= right:
                mid = (left + right)//2
                if arr[mid] == target:
                    ans = mid
                    left = mid + 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans
        
        return [getFO(nums),getLO(nums)]
            
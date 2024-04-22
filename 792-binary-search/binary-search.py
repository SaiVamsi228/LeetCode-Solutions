class Solution:

    def binSearch(self,low,high,target,nums):

        if low > high:

            return -1

        mid = (low+high)//2

        if nums[mid] == target:

            return mid

        elif nums[mid] > target:

            return self.binSearch(low,mid-1,target,nums) 
        
        return self.binSearch(mid+1,high,target,nums)
    def search(self, nums: List[int], target: int) -> int:
        
        return self.binSearch(0,len(nums)-1,target,nums) 
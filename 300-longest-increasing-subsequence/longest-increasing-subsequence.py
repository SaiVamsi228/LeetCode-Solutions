class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def bin_search(arr,num):
        
            left = 0
            
            right = len(arr) - 1
            
            while left <= right :
                
                mid = (left + right)// 2
                
                if num <= arr[mid]:
                    
                    right = mid - 1
                
                else:
                    
                    left = mid + 1
            
            return left
        
        res = [nums[0]]
        
        n = len(nums)
        
        for i in range(1,n):
            
            num = nums[i]
            
            if res == [] or res[-1] < num:
                
                res.append(num)
            
            else:
                
                getPos = bin_search(res,num)
        
                res[getPos] = num
        
        return len(res)
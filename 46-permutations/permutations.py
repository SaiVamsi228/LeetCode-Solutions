class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def findPermutations(arr, start, ans):
    
            if start == len(arr) - 1:
                
                ans.append(arr.copy())
                
                return
            
            mp = set()
            
            for i in range(start, len(arr)):
                if arr[i] not in mp:
                    
                    arr[start], arr[i] =  arr[i], arr[start]
                    
                    findPermutations(arr, start+1, ans)
                    
                    arr[start], arr[i] =  arr[i], arr[start]
                
                    mp.add(arr[i])
            
            return

        ans = []

        findPermutations(nums, 0 , ans)

        return ans
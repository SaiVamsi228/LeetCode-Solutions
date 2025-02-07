class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def getSubset(n,target,subset):

            if target == 0:

                ans.append(subset.copy())

                return 

            if n == 0:

                return 
            
            if candidates[n-1] <= target:

                subset.append(candidates[n-1])

                getSubset(n,target - candidates[n-1],subset)

                subset.pop()
            
            getSubset(n-1,target,subset)
        
        n = len(candidates)

        getSubset(n,target,[])

        return ans
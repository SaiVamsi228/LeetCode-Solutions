class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def getAllSb(n,target,sb):

            if n == 0:

                if target == 0:

                    ans.append(sb.copy())

                return
            
            # take it

            if candidates[n-1] <= target:
                
                sb.append(candidates[n-1])

                getAllSb(n,target - candidates[n-1],sb)
            
                sb.pop()
            
            # dont take it

            getAllSb(n-1,target,sb)
        
        ans = []

        n = len(candidates)

        sb = []

        getAllSb(n,target,sb)

        return ans

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def getAllSb(ind,target,sb):

            if target == 0:

                ans.append(sb.copy())

                return

            if ind == n :

                return
            
            # take it

            for i in range(ind,n):

                if i > ind and candidates[i] == candidates[i-1]:

                    continue # *** BECAUSE FOR THIS PLACE IN THE SUBSET WE ALREADY TOOK THAT ARR[I-1] LET IT BE 1 NOW WHY WOULD WE TAKE THAT 1 AGAIN AS THE SUBSETS ARE ALREADY GENERATED FOR 1

                if candidates[i] <= target:
                    
                    sb.append(candidates[i])

                    getAllSb(i + 1,target - candidates[i],sb)

                    sb.pop()
        
        ans = []

        n = len(candidates)

        candidates.sort()

        sb = []

        getAllSb(0,target,sb)

        return ans

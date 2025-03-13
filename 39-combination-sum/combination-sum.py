class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        
        def get_comb_sums(ind,target,subseq):

            if target == 0:

                ans.append(subseq.copy())

                return

            if ind == n:

                return
            
            if candidates[ind] <= target:

                # take

                subseq.append(candidates[ind])

                get_comb_sums(ind,target - candidates[ind], subseq)

                subseq.pop()

                # not take

                get_comb_sums(ind+1, target, subseq)
            
            else:

                # not take

                get_comb_sums(ind+1, target, subseq)
        
        n = len(candidates)

        get_comb_sums(0, target, [] )

        return ans
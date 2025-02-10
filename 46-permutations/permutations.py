class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        all_perm = permutations(nums)

        ans = []

        for perm in all_perm:

            ans.append(list(perm))
        
        return ans

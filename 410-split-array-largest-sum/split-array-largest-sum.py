class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def getNumberOfSubarrays(sm):

            cur_sm = 0

            sb = 1 # because we assume the first subarr is already started

            n = len(nums)

            for num in nums:

                if cur_sm + num <= sm:

                    cur_sm += num

                else:

                    sb += 1

                    cur_sm = num

            return sb
        
        left = max(nums) # since non-empty

        right = sum(nums)

        ans = right

        while left <= right:

            larg_sm = (left + right)//2

            sb_poss = getNumberOfSubarrays(larg_sm)

            if sb_poss <= k: 

                right = larg_sm - 1

            elif sb_poss > k :

                left = larg_sm + 1
        
        return left








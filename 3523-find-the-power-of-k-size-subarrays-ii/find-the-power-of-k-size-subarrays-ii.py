class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if n == 1 :

            if k == 1:
                
                return [nums[0]]
            
            else:

                return [-1]
        
        if k == 1 :

            return nums

        i = 0

        j = 0

        res = [ -1 for i in range(n-k+1)]

        while j < n :

            if j > 0 and nums[j] != nums[j-1] + 1 :

                i = j

                j += 1

                continue
            
            if j - i + 1 < k :

                j += 1
            
            elif j - i + 1 == k:

                res[i] = nums[j]

                i += 1

                j += 1
            
        return res
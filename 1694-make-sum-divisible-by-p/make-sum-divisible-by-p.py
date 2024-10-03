class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        mod_mp = {0:-1}

        miniLen = len(nums)

        totSum = sum(nums)

        target = totSum % p

        if target == 0:

            return 0

        cS = 0

        for i, num in enumerate(nums):

            cS = (cS + num)%p

            need = (cS - target + p)%p

            if need in mod_mp:

                miniLen = min(miniLen, i - mod_mp[need])
            
            mod_mp[cS] = i

        return miniLen if miniLen != len(nums) else -1
        
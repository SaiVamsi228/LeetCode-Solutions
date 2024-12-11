class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        
        nums.sort()

        n = len(nums)

        dp = [1 for i in range(n)]

        hash_ = [ i for i in range(n)]

        maxi = 1

        lastMaxInd = 0 

        for ind in range(n):

            for prev_ind in range(ind):

                if nums[ind] % nums[prev_ind] == 0 or nums[prev_ind] % nums[ind] == 0 :

                    if  dp[prev_ind] + 1 > dp[ind] :
                        
                        dp[ind] = dp[prev_ind] + 1
                        
                        hash_[ind] = prev_ind

            if dp[ind] > maxi:

                lastMaxInd = ind

                maxi = dp[ind]
        
        res = [nums[lastMaxInd]]

        while lastMaxInd != hash_[lastMaxInd]:
            
            lastMaxInd = hash_[lastMaxInd]

            res.append(nums[lastMaxInd])
        
        print(dp)
        print(hash_)

        return res[::-1]



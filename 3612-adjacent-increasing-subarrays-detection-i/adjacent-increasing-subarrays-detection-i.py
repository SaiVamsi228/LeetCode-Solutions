class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        strictlyInc = [ 1 if i > 0 and nums[i] > nums[i-1] else 0 for i in range(n) ]

        prefix_sum = [0 for i in range(n)]

        prefix_sum[0] = 0

        for i in range(1,n):

            prefix_sum[i] = prefix_sum[i-1] + strictlyInc[i]

        for i in range(n):

            if (i <=  n - 2*k ) and (prefix_sum[i + k - 1] - prefix_sum[i] == k - 1) and (prefix_sum[i + 2*k - 1] - prefix_sum[i + k] == k-1) :

                return True
        
        return False
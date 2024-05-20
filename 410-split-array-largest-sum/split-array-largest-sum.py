class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        low = max(nums)

        high = sum(nums)

        while low <= high :

            largSum = (low + high)//2

            if self.countSubarrays(nums,largSum) <= k:

                high = largSum - 1
            
            else:

                low = largSum + 1

        return low  # if the required partitions < maximum partitions possible 
        # see in case [2,3,1,1,1,1,1] k=5
        # returning when polarity is getting changed
        # RETURN LOW IF MIN IS ASKED 
        # RETURN HIGH IF MAX IS ASKED 

    def countSubarrays(self, nums, maxSum):

        subarrays = 1

        subarraySum = 0

        n = len(nums)

        for i in range(n):

            if subarraySum + nums[i] <= maxSum:

                subarraySum += nums[i]

            else:

                subarrays += 1

                subarraySum = nums[i]

        return subarrays

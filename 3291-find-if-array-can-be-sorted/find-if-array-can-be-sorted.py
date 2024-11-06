class Solution:
    def getNoOfSetBits(self, num):

        bin_ = bin(num)[2:]

        return bin_.count("1")

    def canSortArray(self, nums: List[int]) -> bool:
        
        noOfSetBits = {}

        for num in nums:

            noOfSetBits[num] = self.getNoOfSetBits(num)

        n = len(nums)

        for i in range(1,n):

            while i > 0 and nums[i] < nums[i-1]:

                if noOfSetBits[nums[i]] != noOfSetBits[nums[i-1]]:

                    return False
                
                nums[i], nums[i-1] = nums[i-1] , nums[i]

                i -= 1
        
        return True



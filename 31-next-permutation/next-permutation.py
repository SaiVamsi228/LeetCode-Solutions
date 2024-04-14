from itertools import permutations
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        ind = -1

        for i in range(n-2,-1,-1):

            if nums[i] < nums[i+1] :

                ind = i

                break
        
        if ind == -1:

            nums.sort()

            return nums

        for i in range(n-1,ind,-1):

            if nums[i] > nums[ind]:

                nums[ind],nums[i] = nums[i], nums[ind]

                break
        
        i = ind+1

        j = n-1

        while i < j:

            nums[i] ,nums[j] = nums[j], nums[i]

            i+=1

            j-=1
        
        return nums


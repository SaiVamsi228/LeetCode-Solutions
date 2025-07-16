class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        temp = [float('inf') for i in range(n)]

        i = 0

        j = 1

        for ind in range(n):

            if nums[ind] > 0:

                temp[i] = nums[ind]
            
                i += 2
            
            else:

                temp[j] = nums[ind]

                j += 2
        
        return temp
            


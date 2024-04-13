class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        postInd, negInd = 0, 1

        ans = [0 for i in range(n)]

        for i in range(n):

            if nums[i] > 0:

                ans[postInd] = nums[i]

                postInd += 2
            
            else:

                ans[negInd] = nums[i]

                negInd += 2
            
        return ans
        

                    



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:

            return 0
            
        nums.sort()

        lastSmaller = nums[0]

        n = len(nums)

        longest = 1

        cnt = 1

        for i in range(1,n):

            if nums[i] - 1 == lastSmaller:

                cnt+=1

                lastSmaller = nums[i]
            
            elif nums[i]!=lastSmaller:

                cnt = 1

                lastSmaller = nums[i]
            
            longest = max(longest,cnt)
        

        return longest


                
class Solution:
    def solve(self,nums,n,goal):

        i = j = 0

        cnt = curSum = 0

        while j < n:

            curSum += nums[j]
            
            if curSum > goal:

                while curSum > goal and i < n and i <= j :

                    curSum -= nums[i]

                    i += 1

            if curSum <= goal : #IMP NEED TO CALCULATE AFTER SHRINKING THE WINDOW AS WE MAY LOSE ONE ANS AT THAT INDEX

                cnt += j - i + 1

            j += 1

        return cnt

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        n = len(nums)

        return self.solve(nums,n,goal) - self.solve(nums,n,goal-1)

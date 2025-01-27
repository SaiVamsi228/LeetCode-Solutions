class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        nums.sort()

        res = -1

        cnt = 0

        ans = set()

        for num in nums:

            if cnt == 0 or num != res:

                res = num

                cnt = 1
            
            elif num == res:

                cnt += 1
            
            if cnt > n//3:

                ans.add(res)

        return list(ans)

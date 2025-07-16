from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hm = defaultdict(int)

        hm[0] = 1

        sm = 0

        n = len(nums)

        cnt = 0

        for i in range(n):

            sm += nums[i]
            
            req = sm - k

            if req in hm:

                cnt += hm[req]

            hm[sm] += 1
        
        return cnt
            

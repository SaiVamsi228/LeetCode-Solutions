from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hm = defaultdict(int)
        
        n = len(nums)

        for num in nums:

            hm[num] += 1

        ans = []
        
        for num,freq in hm.items():

            if freq > n/3:

                ans.append(num)
        
        return ans
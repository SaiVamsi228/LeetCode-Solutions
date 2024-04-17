from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)

        h_mp = defaultdict(int)

        pre_sum = 0

        cnt = 0

        h_mp[0] = 1  # MOST IMP: IF K ITSELF EXISTS THEN K-K =0 WHOSE FREQ SHOULD BE 1

        for i in range(n):

            pre_sum += nums[i]

            remove = (pre_sum - k)  
            # IMP : WE ARE VERIFYING IF THERE FORMS A SUBARRAY UPTO INDEX 
            #       I BY SEARCHING FOR X-K IF IT EXISTS THEN IT IS SURE THAT K IS POSSIBLE
            #       IF NUMBER OF X-K SUBARRAYS EXIST THEN WE CAN FORM THAT MANY K SUM SUBARRAYS
            #       WITH DIFFERENT COMBINATIONS SEE STRIVER DIA FOR MORE CLARITY

            cnt += h_mp[remove]

            h_mp[pre_sum] += 1

        return cnt

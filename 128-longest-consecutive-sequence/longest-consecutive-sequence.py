class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:

            return 0
        
        mx = 0

        hs = set([x for x in nums])

        for num in hs:

            if num - 1 not in hs:

                right_consec_len = 1

                rb = num + 1

                while rb in hs:

                    right_consec_len += 1

                    rb += 1
                
                mx = max(mx, right_consec_len)
        
        return mx
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        st = {x for x in nums}

        longest = 1

        for num in st:

            if num - 1 not in st:

                cnt = 0

                while num in st:

                    cnt+=1

                    num+=1
                
                longest = max(longest,cnt)

        
        return longest







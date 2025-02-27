from collections import Counter
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        
        freq_map = Counter(nums)

        for k,v in freq_map.items():

            if v > 2:

                return False

        return True


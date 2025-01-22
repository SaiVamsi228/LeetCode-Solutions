class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        xor_val = start ^ goal

        cnt = 0

        while xor_val > 0:

            xor_val &= xor_val - 1

            cnt += 1
        
        return cnt

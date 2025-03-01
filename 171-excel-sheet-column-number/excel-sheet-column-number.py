class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        ans = 0

        n = len(columnTitle)

        k = 0

        for i in reversed(range(n)):

            ans += (ord(columnTitle[i]) - 64) * 26**(k)

            k += 1
        
        return ans
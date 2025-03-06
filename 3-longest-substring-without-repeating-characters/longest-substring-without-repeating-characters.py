class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)

        mx = 0

        i = j = 0

        hs = set()

        while j < n:

            if s[j] not in hs:

                hs.add(s[j])

                mx = max(mx, j - i + 1)

                j += 1
            
            else:

                while s[j] in hs:

                    hs.discard(s[i])

                    i += 1
                
                hs.add(s[j])
                
                mx = max(mx, j - i + 1)

                j += 1
        
        return mx







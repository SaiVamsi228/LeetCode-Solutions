from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        diff_char_cnt = 0
        mx = 0
        i = j = 0
        n = len(s)
        hm = {}
        max_freq = 0

        while j < n :

            if s[j] in hm:

                hm[s[j]] += 1
            
            else:

                hm[s[j]] = 1
            
            max_freq = max(max_freq,hm[s[j]])

            length_of_str = j - i + 1

            diff_char = length_of_str - max_freq

            if diff_char > k :

                while i <= j and j - i + 1 - max_freq > k:

                    hm[s[i]] -= 1

                    for char,cnt in hm.items():

                        max_freq = max(max_freq,cnt)
                    
                    i += 1
            
            mx = max(mx, j - i + 1 )
            
            j += 1            
        
        return mx

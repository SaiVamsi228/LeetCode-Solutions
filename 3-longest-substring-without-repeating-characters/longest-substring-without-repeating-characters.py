from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mx_len = 0

        hash_map = defaultdict(int)

        dist_cnt = 0

        i = j = 0

        n = len(s)

        while j < n :

            char = s[j]

            hash_map[char] += 1

            if hash_map[char] > 1 :

                dist_cnt += 1
            
            if dist_cnt == 0 :

                mx_len = max(mx_len,j-i+1)
            
            elif dist_cnt > 0:

                while dist_cnt > 0 and i <= j :

                    hash_map[s[i]] -= 1

                    if hash_map[s[i]] == 1 :

                        dist_cnt -= 1

                    i += 1
                
                if dist_cnt == 0:

                    mx_len = max(mx_len, j - i + 1)
                
            j += 1
        
        return mx_len
            

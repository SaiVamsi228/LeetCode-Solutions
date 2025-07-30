from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        i = j = 0

        n = len(s)

        req_hm = {}

        for char in t:

            if char in req_hm:

                req_hm[char] += 1
            
            else:

                req_hm[char] = 1

        req_satis_cnt = len(req_hm)

        hm = defaultdict(int)

        satis_cnt = 0

        mn = float('inf')

        mn_sub_str = ""

        while j < n :

            char = s[j]

            if char not in req_hm:

                j += 1

                continue

            hm[char] += 1

            if hm[char] == req_hm[char]:

                satis_cnt += 1
            
            if satis_cnt < req_satis_cnt :

                j += 1

                continue
            
            elif satis_cnt == req_satis_cnt:
                
                # shrinking size as much as we can for mn substring
                while i <= j :

                    left_char = s[i]

                    if left_char not in req_hm:

                        i += 1

                        continue

                    if hm[left_char] - 1 < req_hm[left_char]:

                        break
                    
                    elif hm[left_char] - 1 >= req_hm[left_char]:

                        hm[left_char] -= 1

                        i += 1
                
                sub_str_len = j - i + 1

                if sub_str_len < mn:

                    mn = sub_str_len

                    mn_sub_str = s[i:j+1]

                j += 1

        return mn_sub_str






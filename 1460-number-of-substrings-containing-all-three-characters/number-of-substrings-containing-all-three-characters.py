class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        hm = {}

        i = j = 0

        n = len(s)

        cnt = 0

        uniq_char = 0

        while j < n :

            char = s[j]

            if char in hm:

                hm[char] += 1
            
            else:

                hm[char] = 1

                uniq_char += 1
            
            if uniq_char < 3 :

                j += 1
            
            elif uniq_char == 3:

                cnt += n - j

                while i <= j and uniq_char == 3 :

                    hm[s[i]] -= 1

                    if hm[s[i]] == 0:

                        del hm[s[i]]

                        uniq_char -= 1
                    
                    if uniq_char == 3:

                        cnt += n - j

                    i += 1
                
                j += 1
        
        return cnt
                


            


            


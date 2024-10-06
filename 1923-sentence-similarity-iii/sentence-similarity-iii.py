class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        a = list(sentence1.split()) 

        b = list(sentence2.split())

        s = a if len(a) <= len(b) else b

        l = a if len(a) > len(b) else b

        m = len(s)

        n = len(l)


        i1, j1 = 0 , m - 1

        i2, j2 = 0 , n - 1

        while i1 <= j1 and i2 <= j2 and (s[i1] == l[i2] or s[j1] == l[j2]):

            if s[i1] == l[i2]: 

                i1 += 1

                i2 += 1

            else:

                j1 -= 1

                j2 -= 1

        if i1 > j1 : return True

        return False 
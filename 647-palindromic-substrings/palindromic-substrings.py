class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        c = 0

        for i in range(n):
            # odd length palindromes
            j = k = i
            while j >= 0 and k < n and s[j] == s[k]:
                c += 1
                j -= 1
                k += 1

            # even length palindromes
            j, k = i, i + 1
            while j >= 0 and k < n and s[j] == s[k]:
                c += 1
                j -= 1
                k += 1

        return c

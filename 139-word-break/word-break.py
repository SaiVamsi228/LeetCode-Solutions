class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        def isPossible(current,memo):

            if current in memo:

                return memo[current]
            
            if not current:

                return True
            
            for word in wordDict:

                if current.startswith(word):

                    new_current = current[len(word):]

                    if isPossible(new_current,memo):

                        memo[current] = True

                        return True
            
            memo[current] = False

            return False

        memo = {}
        
        n = len(s)

        return isPossible(s,memo)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        q = deque()

        q.append(beginWord)

        step = 1

        wordList = set(wordList)

        hs = set()

        hs.add(beginWord)

        while q:
                        
            t = len(q)

            step += 1

            for _ in range(t):
                
                word = q.popleft()

                for i,char in enumerate(word):

                    for new_letter in "abcdefghijklmnopqrstuvwxyz":

                        if char == new_letter:

                            continue
                        
                        new_word = word[:i] + new_letter + word[i+1:]

                        if new_word in hs:

                            continue
                        
                        if new_word in wordList:

                            hs.add(new_word)

                            q.append(new_word)
                            
                            if new_word == endWord:

                                return step
        
        return 0
        


                        
                        
            






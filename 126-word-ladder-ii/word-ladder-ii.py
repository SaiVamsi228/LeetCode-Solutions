from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if endWord not in wordList:
            
            return []

        
        hm = {}

        q = deque()

        dist = 0

        q.append((beginWord,dist))

        wordSet = set(wordList)

        while q:

            word, dist = q.popleft()

            if word == endWord:

                hm[endWord] = dist

                break

            if word in hm:
                
                continue  # already visited
            
            hm[word] = dist

            for i in range(len(word)):

                for j in range(26):

                    new_char = chr(ord('a') + j)

                    if new_char == word[i]:

                        continue

                    new_word = word[:i] + new_char + word[i+1:]

                    if new_word in wordSet:

                        wordSet.discard(new_word)

                        q.append((new_word,dist + 1))

        ans = []

        def genSequences(word,beginWord,path):

            if word == beginWord:

                ans.append(path.copy()[::-1])

                return 
            
            for i in range(len(word)):

                for j in range(26):

                    new_char = chr(ord('a') + j)

                    if new_char == word[i]:

                        continue

                    new_word = word[:i] + new_char + word[i+1:]

                    if new_word in hm and hm[new_word] == hm[word] - 1:

                        path.append(new_word)

                        genSequences(new_word,beginWord,path)

                        path.pop()
        
        if endWord in hm:
            
            genSequences(endWord,beginWord,[endWord])

        return ans
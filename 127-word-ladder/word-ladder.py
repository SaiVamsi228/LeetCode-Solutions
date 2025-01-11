from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet = set(wordList)
        
        q = deque()

        q.append((beginWord,1))

        while q:

            curWord, dist = q.popleft()

            if curWord == endWord :

                return dist

            for i in range(len(curWord)):

                for ch in "abcdefghijklmnopqrstuvwxyz":

                    if ch == curWord[i] :

                        continue

                    newWord = curWord[:i] + ch + curWord[i+1:]

                    if newWord in wordSet:

                        wordSet.discard(newWord)

                        q.append((newWord,dist+1))
        
        return 0
                







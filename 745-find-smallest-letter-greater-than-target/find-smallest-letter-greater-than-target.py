class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        nextGreater = letters[0]

        n = len(letters)

        low , high = 0, n - 1

        found = False

        while low <= high:

            mid = (low + high)//2

            if letters[mid] == target:

                found = True
            
                low = mid + 1
            
            if letters[mid] < target:

                low = mid + 1
            
            if letters[mid] > target:

                nextGreater = letters[mid]

                high = mid - 1
        
        return nextGreater
class HelperMethod:
    # Find the next smaller element
    def nextSmaller(self, arr):
        n = len(arr)
        nse = [n] * n
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and arr[stk[-1]] > arr[i]:
                stk.pop()
            nse[i] = stk[-1] if stk else n
            stk.append(i)
        return nse

    # Find the previous smaller element
    def previousSmaller(self, arr):
        n = len(arr)
        pse = [-1] * n
        stk = []
        for i in range(n):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop()
            pse[i] = stk[-1] if stk else -1
            stk.append(i)
        return pse


class Solution:
    def sumSubarrayMins(self, arr):
        helper = HelperMethod()  # Create an object to access helper methods
        nextSE = helper.nextSmaller(arr)
        prevSE = helper.previousSmaller(arr)
        total = 0
        mod = int(1e9 + 7)

        for i in range(len(arr)):
            left = i - prevSE[i]
            right = nextSE[i] - i
            total = (total + left * right * arr[i]) % mod

        return total

# Usage example:
# solution = Solution()
# print(solution.sumSubarrayMins([3,1,2,4]))  # Example input

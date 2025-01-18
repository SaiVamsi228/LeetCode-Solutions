class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        
        sorted_cost = k

        n = len(arr)

        sorted_arr = sorted(arr)

        sorted_brr = sorted(brr)

        for i in range(n):

            sorted_cost += abs(sorted_arr[i] - sorted_brr[i])

        unsorted_cost = 0

        for i in range(n):

            unsorted_cost += abs(arr[i] - brr[i])
        
        return min(sorted_cost, unsorted_cost)
        



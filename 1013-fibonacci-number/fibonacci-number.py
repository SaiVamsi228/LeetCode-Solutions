class Solution:
    def fib(self, n: int) -> int:

        first = 0

        if n == 0:

            return first

        second = 1

        if n == 1 :

            return second
        
        for i in range(2,n+1):

            third = first + second

            first = second

            second = third

        return third


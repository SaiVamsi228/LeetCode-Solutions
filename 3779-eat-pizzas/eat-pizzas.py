class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        
        n = len(pizzas)

        total_days = n//4

        even_days = (n//4)//2

        odd_days = total_days - even_days

        pizzas.sort(reverse = True)

        weight = sum(pizzas[:odd_days])

        i = odd_days

        while even_days:

            weight += pizzas[i+1]

            i += 2

            even_days -= 1
        
        return weight





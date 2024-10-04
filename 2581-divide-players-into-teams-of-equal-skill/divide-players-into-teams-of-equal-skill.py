class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        n = len(skill)

        i = 0

        j = n - 1

        target = skill[i] + skill[j]

        chem = skill[i] * skill[j]

        i += 1

        j -= 1

        while i < j :

            if skill[i] + skill[j] != target:

                return -1
            
            else:

                chem += skill[i] * skill[j]

                i += 1

                j -= 1
        
        return chem

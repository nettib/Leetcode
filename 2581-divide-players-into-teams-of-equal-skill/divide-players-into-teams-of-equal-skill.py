class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        com=0
        chem=0
        left=0
        right=len(skill)-1
        if len(skill)==2:
            return skill[left]*skill[right]
        else:
            com=skill[left]+skill[right]
            while left<right:
                if skill[left]+skill[right]==com:
                    chem+=(skill[left]*skill[right])
                    left+=1
                    right-=1
                else:
                    return -1
        return chem

            


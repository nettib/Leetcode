class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        check_skill = 0
        chem = 0
        l, r = 0, len(skill) - 1
        while l < r:
            team_skill = skill[l] + skill[r]
            if check_skill != 0 and team_skill != check_skill:
                return -1
            else:
                chem += skill[l] * skill[r]
                check_skill = team_skill
            l += 1
            r -= 1
        
        return chem
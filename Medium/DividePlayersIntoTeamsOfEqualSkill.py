class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        if len(skill) == 2:
            return skill[0] * skill[1]
        skill.sort()
        x = 0
        y = len(skill) - 1
        equal = skill[x] + skill[y]
        res = skill[x] * skill[y]
        x += 1
        y -= 1
        while x < y:
            if not skill[x] + skill[y] == equal:
                return -1
            res += skill[x] * skill[y]
            x += 1
            y -= 1
        return res
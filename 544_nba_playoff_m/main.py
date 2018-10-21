class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        matches = [1]
        teams = 1
        while teams < n:
            teams *= 2
            previous_round = []
            for e in matches:
                if isinstance(e, int):
                    previous_round.extend(["(", e, ",", teams + 1 - e, ")"])
                else:
                    previous_round.append(e)
            matches = previous_round
        return "".join(map(str, matches))
        
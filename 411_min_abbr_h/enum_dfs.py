class Solution(object):

    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            jj = j
            while jj < len(abbr) and abbr[jj].isdigit():
                jj += 1
            
            if jj > j and abbr[j] != '0':
                occur = int(abbr[j:jj])
                # handle i out of range outside
                i, j = i + occur, jj
            elif word[i] != abbr[j]:
                return False
            else:
                i, j = i + 1, j + 1
        
        return i == len(word) and j == len(abbr)

    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        self.min_abbr = None

        def dfs(i, abbr):
            # Check solution
            if i == len(target):
                check_update_solution(abbr)
            else:
                dfs(i + 1, abbr + [target[i]]) # add alphabet
                if len(abbr) > 0 and isinstance(abbr[-1], int):
                    dfs(i + 1, abbr[:len(abbr) - 1] + [abbr[-1] + 1])
                else:
                    dfs(i + 1, abbr + [1])
    
        def check_update_solution(abbr):
            if self.min_abbr == None or len(abbr) < len(self.min_abbr):
                abbr_str = "".join(map(str, abbr))
                if all(not self.validWordAbbreviation(w, abbr_str) for w in dictionary):
                    self.min_abbr = abbr

        dfs(0, [])
        return "".join(map(str, self.min_abbr))
    
# Passes slightly
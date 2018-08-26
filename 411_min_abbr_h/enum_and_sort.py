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
        
        # First enumerate all the abbrs
        # "" does not have "0" as abbr
        abbrs = [[]]
        for i in range(len(target)):
            new_abbrs = []
            for abbr in abbrs:
                new_abbrs.append(abbr + [target[i]])
                if len(abbr) > 0 and isinstance(abbr[-1], int):
                    new_abbrs.append(abbr[:len(abbr) - 1] + [abbr[-1] + 1])
                else:
                    new_abbrs.append(abbr + [1])
            abbrs = new_abbrs
        
        # Sort by length
        abbrs = sorted(abbrs, key=lambda x:len(x))
        
        
        for abbr in abbrs:
            dup_flag = False
            abbr_str = "".join(map(str, abbr))
            for w in dictionary:
                if self.validWordAbbreviation(w, abbr_str):
                    dup_flag = True
            
            if not dup_flag:
                return abbr_str
        
        return False

# Too expensive to check all abbr of dictionary, however, not so expensive to enumerate the abbr of target.
# and use the function of 408 to verify against each word in dictionary
# 
# This solution is MLE
# 
# To solve the problem , use DFS see enum_and_sort.py
# 
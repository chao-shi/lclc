class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        m1, m2 = {}, {}
        def recur(i, j):
            if i == len(pattern) and j == len(str):
                return True
            elif i == len(pattern) or j == len(str):
                return False
            elif pattern[i] in m1:
                word = m1[pattern[i]]
                return word == str[j:j+len(word)] and recur(i + 1, j + len(word))
            else:
                for jend in range(j + 1, len(str) + 1):
                    word = str[j:jend]
                    if word in m2:
                        continue
                    m1[pattern[i]] = word
                    m2[word] = pattern[i]
                    if recur(i + 1, j + len(word)):
                        return True
                    del m1[pattern[i]]
                    del m2[word]
                return False
        
        return recur(0, 0)

# Block 12 careful
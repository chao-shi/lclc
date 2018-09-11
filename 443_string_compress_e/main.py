class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        j = 0
        while i < len(chars):
            print i
            ii = i
            while i < len(chars) and chars[i] == chars[ii]:
                i += 1

            chars[j] = chars[ii]
            j += 1
            
            if i - ii > 1:
                rep = str(i - ii)
                chars[j: j + len(rep)] = str(i - ii)
                j += len(rep)
        return j
        
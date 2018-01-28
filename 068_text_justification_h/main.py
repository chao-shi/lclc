class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        left = 0
        lines = []
        while left < len(words):
            remain = maxWidth
            right = left
            while right < len(words) and remain >= len(words[right]):
                remain -= (len(words[right]) + 1)
                right += 1
            
            wcnt = right - left

            if right == len(words) or wcnt == 1: 
                line = " ".join(words[left:right])
                lines.append(line + " " * (maxWidth - len(line)))
            else:
                spaces = remain + cnt
                more_spaces_num = spaces % (wcnt - 1)
                spaces_per_seg = spaces / (wcnt - 1)
                
                line = words[left]
                for i in range(left+1, right):
                    line += " " * spaces_per_seg
                    if i - left <= more_spaces_num:
                        line += " "
                    line += words[i]
                lines.append(line)
            left = right
        return lines

# Trick on block 13 and trick on line 23.
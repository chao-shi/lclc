class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return "".join(map(lambda x:x.replace("\\", "\\\\").replace("|", "\\|") + "|", strs))

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
        word = ""
        while i < len(s):
            if s[i] == "\\":
                word += s[i+1]
                i += 1
            elif s[i] == "|":
                res.append(word)
                word = ""
            else:
                word += s[i]
            i += 1
        return res

# Wrong thinking: 
# 1. Using delimiter, then we cannot differetiate between [""] and []
# 2. Use split() to decode is not possible, confuse between "|" and "\|"

# Correct way
# 1. Add ending special char at the end
# 2. When decoding, skip the special character and read next

# Another approach: header (length) + body

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
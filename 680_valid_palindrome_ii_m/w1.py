class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i, j = i + 1, j - 1
            elif not flag:
                return False
            elif s[i + 1] == s[j]:
                i += 1
                flag = False
            elif s[j - 1] == s[i]:
                j -= 1
                flag = False
            else:
                return False
            print s[:i+1], s[j:], flag
        return True

# Does not pass "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"

# block 14 and block 17 will fail in the following case
# ab    and     ab
# when i at left a and j at right b
# Cannot decide which to take
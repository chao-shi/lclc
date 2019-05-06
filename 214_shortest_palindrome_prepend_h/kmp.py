class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # longest proper prefix suffix map
        def make_lps(s):
            lps = [0] * len(s)
            for i in range(1, len(s)):
                len_cand = lps[i-1]
                while s[len_cand] != s[i]:
                    if len_cand == 0:
                        len_cand = -1
                        break
                    else:
                        len_cand = lps[len_cand - 1]
                lps[i] = len_cand + 1
            return lps

        def longest_palin_prefix(s):
            lps = make_lps(s)
            r = s[::-1]

            # r[i-j:i] with s[:j] already matched
            i, j = 0, 0
            while i < len(s):
                if r[i] == s[j]:
                    i, j = i + 1, j + 1
                else:
                    # s shift relatively right to r
                    # j decrement if can
                    # otherwise i += 1
                    if j > 0:
                        j = lps[j-1]
                    else:
                        i += 1
            return j
        
        longest_prefix = longest_palin_prefix(s)
        return s[longest_prefix:][::-1] + s

# TODO Runtime Analysis

# Focus on j, when j increments i also increments. 
# N(j_incr) <= N(i_incr) <= len(s) (beacuse of while loop exit condition)
# N(j_decr) <= N(j_incr) (j has lower bound of zero)
# Therefore N(i_incr) + N(j_incr) + N(j_decr) is O(N)
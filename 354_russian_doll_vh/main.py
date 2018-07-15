class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes = sorted(envelopes, key=lambda env:(env[0], -env[1]))
        h_seq = []
        
        for env in envelopes:
            idx = bisect.bisect_left(h_seq, env[1])
            if idx == len(h_seq):
                h_seq.append(env[1])
            else:
                h_seq[idx] = env[1]
        return len(h_seq)

# Sort by W and maintain longest sequence of increasing H for each sequence length
# The job of each new doll is to optimize the H
# Why: he does not need to worry about W, since the later comers have even bigger W

# The only problem is that he may attach new evenlope outside some doll of same W

# To prevent this from happening, the trick is to sort the doll by H reversed after sorting W.

# How the sorting works, use key lambda function
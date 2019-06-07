import sys
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.minlen = sys.maxint
        self.minseq = None
        def recur(seq, covered, base):
            if len(seq) > self.minlen:
                return
            elif len(covered) == base ** n:
                if len(seq) < self.minlen:
                    self.minlen = len(seq)
                    self.minseq = seq
            else:
                prefix = seq[len(seq) - n + 1:]
                for d in range(k):
                    newcode = prefix + str(d)
                    if newcode not in covered:
                        covered.add(newcode)
                        recur(seq + str(d), covered, base)
                        covered.remove(newcode)

        covered = set()
        covered.add("0" * n)
        recur("0" * n, covered, k)
        return self.minseq

# Starting with all zero is a bold assumption, but seems working
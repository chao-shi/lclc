class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def nums_n_digits(n, limit):
            return [num for num in range(limit) if bin(num).count('1') == n]

        ret = []
        for i in range(max(num, 4) + 1):
            j = num - i
            if j <= 6:
                nis = nums_n_digits(i, 12)
                njs = nums_n_digits(j, 60)
                ret.extend([str(ni) + ":" + '{num:02d}'.format(num=nj) for ni in nis for nj in njs])
        return ret

# Function 7: simple solution is best when input is small.
# for bigger problems, we may use permutation of n instance of 1
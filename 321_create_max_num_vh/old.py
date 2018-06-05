class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n, m = len(nums1), len(nums2)

        a1 = [[""] * (n + 1) for i in range(n+1)]
        a2 = [[""] * (m + 1) for i in range(m+1)]

        for i in range(n-1, -1, -1):
            for t in range(1, min(k, n - i) + 1):
                a1[i][t] = max(a1[i+1][t], str(nums1[i]) + a1[i+1][t-1])

        for i in range(m-1, -1, -1):
            for t in range(1, min(k, m - i) + 1):
                a2[i][t] = max(a2[i+1][t], str(nums2[i]) + a2[i+1][t-1])

        maxconcat = ""
        for i1 in range(max(0, k-m), min(k, n) + 1):
            i2 = k - i1
            maxconcat = max(maxconcat, self.merge(a1[0][i1], a2[0][i2]))

        return [int(s) for s in list(maxconcat)]

    def merge(self, s1, s2):
        n, m = len(s1), len(s2)
        i, j = 0, 0
        merged = ""
        while i < n or j < m:
            if i == n:
                merged = merged + s2[j]
                j += 1
            elif j == m :
                merged = merged + s1[i]
                i += 1
            elif s1[i] < s2[j]:
                merged = merged + s2[j]
                j += 1
            elif s1[i] > s2[j]:
                merged = merged + s1[i]
                i += 1
            else:
                ii, jj = i + 1, j + 1
                while ii < n and jj < m and s1[ii] == s2[jj]:
                    ii, jj = ii + 1, jj + 1

                if ii == n:
                    move1 = False
                elif jj == m or s1[ii] > s2[jj]:
                    move1 = True
                else:
                    move1 = False

                if move1:
                    merged = merged + s1[i]
                    i += 1
                else:
                    merged = merged + s2[j]
                    j += 1

        return merged
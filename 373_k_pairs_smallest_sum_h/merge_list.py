from Queue import PriorityQueue

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []
        pq = PriorityQueue()
        # each num2 will keep an anchor on nums1 of what is the next candidate.
        # choose min from next candidate and increment its anchor
        # each num2 represent a list to merge
        for i in range(len(nums2)):
            pq.put((nums2[i] + nums1[0], 0, i))

        res = []
        while len(res) < k and pq.qsize() > 0:
            _, i, j = pq.get()
            res.append((nums1[i], nums2[j]))
            if i < len(nums1) - 1:
                pq.put((nums1[i+1] + nums2[j], i+1, j))
        return res

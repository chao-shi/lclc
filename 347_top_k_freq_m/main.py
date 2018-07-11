import Queue
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
        pq = Queue.PriorityQueue()
        
        for num, f in cnt.items():
            pq.put((f, num))
            if pq.qsize() > k:
                pq.get()
            
        return [num for _, num in pq.queue]

# Complexity 
# n * logk
# Narrow down it is actually 
# k + (n - k) * logk
# The first k element is like heapify

# PriorityQueue
# put(), get(), qsize(), pq.queue[0] to get top

# If we are using PQ already, DON'T DON'T compare with head
# blindly put into queue and use size to determine if to pop

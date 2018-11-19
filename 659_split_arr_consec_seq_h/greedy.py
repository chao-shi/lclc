class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # key is last element, value is list of length for each consecutive sub array ending at key
        # sorted by length reverse
        last_len_map = collections.defaultdict(collections.deque)

        for num in nums:
            if last_len_map[num - 1]:
                # Takes the current shortest from num - 1, and put at the top of list at num 
                l = last_len_map[num - 1].pop()
                last_len_map[num].appendleft(l + 1)
            else:
                last_len_map[num].append(1)
        
        for num in last_len_map:
            if last_len_map[num] and last_len_map[num][-1] < 3:
                return False
        return True

# greedily extending shorter subsequence
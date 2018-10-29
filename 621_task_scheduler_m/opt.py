class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # Selecting N + 1 at a time, there can always be guarantee a way to arrange inside 
        # two N + 1 windows so that no same task are within N apart.

        cnt_map = collections.defaultdict(int)
        for t in tasks:
            cnt_map[t] += 1
        all_chars = set(cnt_map)

        remain = len(tasks)
        time = 0
        
        while remain > 0:
            # top n chars with remaining counter
            sorted_chars = sorted(all_chars, key=lambda x:-cnt_map[x])
            
            # Pick those with remaining cnt > 0
            cands = filter(lambda x:cnt_map[x] > 0, sorted_chars[:n + 1])
            
            remain -= len(cands)
            
            time += len(cands) if remain == 0 else n + 1

            for ch in cands:
                cnt_map[ch] -= 1
        return time
            
    
# Since we don't care about the exact sequence, we can process N+1 window at a time
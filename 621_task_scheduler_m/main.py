class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt_map = collections.defaultdict(int)
        for t in tasks:
            cnt_map[t] += 1

        res = []
        # word in the window of n, cannot have two same task
        bag = set()
        remain = len(tasks)
        
        while remain > 0:
            max_cnt, max_ch = 0, None
            for ch in cnt_map:
                if ch not in bag and cnt_map[ch] > max_cnt:
                    max_cnt = cnt_map[ch]
                    max_ch = ch
            
            if max_ch == None:
                res.append("idle")
            else:
                cnt_map[max_ch] -= 1
                bag.add(max_ch)
                res.append(max_ch)
                remain -= 1

            if len(res) - n - 1 >= 0:
                t1 = res[len(res) - n - 1]
                if t1 != "idle":
                    bag.remove(t1)
        return len(res)
    
# Similar to CPU idea of shortest remaining time first.
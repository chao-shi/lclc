import collections
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        robbed_time = collections.defaultdict(int)
        run_time = collections.defaultdict(int)

        for log in logs:
            fid, event, ts = log.split(":")
            fid, ts = int(fid), int(ts)

            if event == "start":
                stack.append((fid, ts))
            elif event == "end":
                duration = ts + 1 - stack.pop()[1]
                run_time[fid] += duration
                if stack:
                    robbed_time[stack[-1][0]] += duration

        return [run_time[i] - robbed_time[i] for i in range(n)]                
        
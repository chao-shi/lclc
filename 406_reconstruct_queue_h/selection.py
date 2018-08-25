class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        counter = [p + [p[1]] for p in people]
        for i in range(len(people)):
            # select part, find the candidate
            cand = i
            for j in range(i + 1, len(counter)):
                if counter[j][2] < counter[cand][2] or (counter[j][2] == counter[cand][2] and counter[j][0] < counter[cand][0]):
                    cand = j

            # swap cand with i, put permanently on i
            counter[i], counter[cand] = counter[cand], counter[i]

            # Update on the remain
            for j in range(i + 1, len(counter)):
                if counter[j][0] <= counter[i][0]:
                    counter[j][2] -= 1
        return map(lambda p:p[0:2], counter)
            
# Selection sort
# counter keeps (h, k, remain) remain is how many bigger in addition to the currents in the result are still needed.

# Each time, we pick the smallest remain, if multiple smallest remain, we pick smallest k. (Line 18)

# Once we know which to go to the final result, update the remain to the unselected ones.
        
# First I think about one time sorting. But too many moving around things on the final result
# Instead, we will use something similar to selection sorting. Put element in final result one by one
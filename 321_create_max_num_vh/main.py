class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # Brilliant idea of greedy algorithm
        def make_largest(num, k):
            # Must be solvable using O(N + K)
            # Similar to #316
            # Make a special judgement to see if cur is to pop the last
            # Here the judgement is if there are still enough values to use
            
            stack = []
            for (i, n) in enumerate(num):
                while stack and stack[-1] < n and len(stack) + (len(num) - i - 1) >= k:
                    # cur replace last in stack, still len(num) - i - 1 available
                    stack.pop()
                if len(stack) < k:
                    stack.append(n)
            return stack
                
        # This merge check the first different char in the prefix, which covers the traditional 
        # first char comparison as well
        def merge(s1, s2):
            i, j = 0, 0
            res = []
            while len(res) < len(s1) + len(s2):
                ii, jj = i, j
                while ii < len(s1) and jj < len(s2) and s1[ii] == s2[jj]:
                    ii, jj = ii + 1, jj + 1
                
                if jj == len(s2) or (ii < len(s1) and s1[ii] > s2[jj]):
                    # take s1
                    res.append(s1[i])
                    i += 1
                else:
                    res.append(s2[j])
                    j += 1
            return res
                    
                   
        max_v = None
        for k1 in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            k2 = k - k1
            seq1, seq2 = make_largest(nums1, k1), make_largest(nums2, k2)
            merged = merge(seq1, seq2)
            merged_str = "".join(map(str, merged))
            if max_v == None or merged_str > max_v:
                max_v = merged_str
        return map(int, list(max_v))
        
# Main idea, split k into k1 from nums1 and k2 from nums2.
# Solve each problem using greedy algorithm (stack with constraints)
# Then merge it

# Complexity K * (M + N)

# The merge is very very tricky in case of equal
# for example, merge [2] and [2, 6]
# In the code if always take first one when equal
# The result will be [2, 2, 6] while the correct result is [2, 6, 2]

# The merge is not to compare the first digit but iterate until first different met
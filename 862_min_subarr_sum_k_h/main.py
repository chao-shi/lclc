class Solution():
    def mink(self, A, K):
        stack = [0]
        accu = [0]
        accu_sum = 0
        for num in A:
            accu_sum += num
            accu.append(accu_sum)

        j = 0

        min_win = len(A) + 1

        for i in range(1, len(accu)):
            while stack and accu[stack[-1]] > accu[i]:
                stack.pop()
            stack.append(i)

            # check for out of boundary stack pointer
            if j >= len(stack):
                j = len(stack) - 1

            # Case 1, insert a larger accu without any popping, should move j 
            # 
            # Case 2, if something was popped, then now this is true
            # accu[stack[-1]] - accu[stack[j]] < k
            # Why: j did not move yet and accu[stack[-1]] becomes smaller
            # 
            # Case 2 will skip the loop
            while j < len(stack) and accu[stack[-1]] - accu[stack[j]] >= K:
                j += 1

            if j > 0 and accu[stack[-1]] - accu[stack[j-1]] >= K:
                min_win = min(min_win, stack[-1] - stack[j-1])

        return -1 if min_win == len(A) + 1 else min_win

print Solution().mink([2,-1,2], 3)
print Solution().mink([-28,81,-20,28,-29], 89)
            
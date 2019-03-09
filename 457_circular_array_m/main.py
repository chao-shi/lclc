class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # The purpose is to clean out values
        # everything maps between [-len, 0) and (0, len]
        # So that ranges outside can be used to mark additional info
        def clean_number(nums):
            for i, num in enumerate(nums):
                if abs(num) > len(nums):
                    if num > 0:
                        num %= len(nums)
                        if num == 0:
                            num = len(nums)
                    else:
                        num = num % len(nums) - len(nums)
                nums[i] = num
            return nums
        
        nums = clean_number(nums)

        # Move from state i to next and at the same time mark state i as visited.
        # forward = None means no care
        # forward = True means must move forward, return None if cannot
        def move_and_mark(i, forward=None):
            if i == None:
                return None
            
            flag = is_forward(i)
            if forward != None and flag != forward:
                return None

            i = i + nums[i]
            i %= len(nums)
            return i            
            

        def is_forward(i):
            return nums[i] > 0

        
        def test_start(i):
            s, f = i, i
            cnt = 0
            forward_flag = is_forward(s)
            while cnt == 0 or s != f:
                s = move_and_mark(s, forward_flag)
                f = move_and_mark(move_and_mark(f, forward_flag), forward_flag)
                if s == None or f == None:
                    return False
                cnt += 1

            loop_cnt = 0
            while loop_cnt == 0 or s != f:
                s = move_and_mark(s)
                f = move_and_mark(move_and_mark(f))
                loop_cnt += 1
            
            return loop_cnt > 1
        
        return any(test_start(i) for i in range(len(nums)))
            
# [3, 2, 1, 1, 2] Failed, the question asked forward or backward loop only.
# 0, 3, 1, 2, 1
# 
# Skip the visited state from full.py
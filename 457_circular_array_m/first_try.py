class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def move(i, step, length):
            i += step
            if i < 0:
                i += length
            return i % length
        
        nums = [move(i, num, len(nums)) for i, num in enumerate(nums)]
        
        # Move from state i to next and at the same time mark state i as visited.
        def move_and_mark(i):
            if nums[i] < len(nums):
                nums[i] += len(nums)
            return nums[i] - len(nums)

        def test_start(i):
            if nums[i] >= len(nums):
                return False
            
            s, f = i, i
            cnt = 0
            while cnt == 0 or s != f:
                s = move_and_mark(s)
                f = move_and_mark(move_and_mark(f))
                cnt += 1

            loop_cnt = 0
            while loop_cnt == 0 or s != f:
                s = move_and_mark(s)
                f = move_and_mark(move_and_mark(f))
                loop_cnt += 1
            
            return loop_cnt > 1
        
        return any(test_start(i) for i in range(len(nums)))

# Problem of storing the next index (instead of delta)
# If next arrival is 0. We cannot know if it is forward of backward loop.
# 
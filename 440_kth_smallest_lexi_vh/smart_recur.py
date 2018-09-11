class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def next_row_start(num):
            return num * 10 if num != 0 else 1

        # Count size of complete tree, level by level
        def tree_size(num):
            cnt = 0
            level_cnt = 1
            while num <= n:
                cnt += min(n - num + 1, level_cnt)
                level_cnt *= 10
                # num *= 10
                num = next_row_start(num)
            return cnt
        
        # Find answer which is offset of num
        # Return answer if that number is under the tree
        # Otherwise, return the new offset
        def recur(num, offset):
            if offset == 0:
                return num, 0

            # t_size is like the array length
            t_size = tree_size(num)
            if offset >= t_size:
                return None, offset - t_size
            else:
                offset -= 1
                row_start = next_row_start(num)
                for ch in range(row_start, row_start + 10):
                    target, offset = recur(ch, offset)                    
                    if target != None:
                        return target, offset
        
        
        # Think about k as the index of stream [0, 1, 10, 100, 101, ...]
        target, _ = recur(0, k)
        return target

# Key idea is how to aboid visiting everything under the root of the tree.the
# We already know the tree is complete. So this is something to take advantage of.
# 
# If the offset is smaller than size of tree, the answer is under the tree. 
# We need to go through all the children
# 
# Otherwise, we know the answer is outside of the subtree. So subtract offset with the
# tree size. line 32.
# 
# Careful points:
# next_row_start, not * 10, does not work for 0, 1 case
# 
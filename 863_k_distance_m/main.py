# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.Tpath = None

        def findTPath(root, path):
            if not root:
                return
            elif root == target:
                self.Tpath = list(path)
            else:
                path.append(root.left)
                findTPath(root.left, path)
                path[-1] = root.right
                findTPath(root.right, path)
                path.pop()

        findTPath(root, [root])
        Tpath = self.Tpath
        res = []
        print map(lambda x:x.val, Tpath)
        
        # mypath is the current path for root
        # i is where mypath last meet with Tpath
        def recur(root, mypath, i):
            if root == None:
                return

            if i + 1 < len(Tpath) and Tpath[i+1] == root:
                i += 1
            mypath.append(root)
            
            distance = len(mypath) - i + len(Tpath)- i - 2
            print root.val, map(lambda x:x.val, mypath), i, distance

            if distance == K:
                res.append(root.val)
            
            if distance < K or i == len(mypath) - 1:
                # Don't forget second condition
                # distance < K or even bigger than K but still hasn't branched
                recur(root.left, mypath, i)
                recur(root.right, mypath, i)
            mypath.pop()
        
        recur(root, [], -1)
        return res
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        files = path.split("/")
        stack = []
        for f in files:
            if f == "..":
                if stack:
                    stack.pop()
            elif f != "" and f != '.':
                stack.append(f)
        return "/" + "/".join(stack)

#Careful line 10 case
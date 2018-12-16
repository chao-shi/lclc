"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        sub_map = {}
        imp_map = {}
        for e in employees:
            eid, imp, subs = e.id, e.importance, e.subordinates
            imp_map[eid] = imp
            sub_map[eid] = subs
        
        def recur(root):
            return imp_map[root] + sum(recur(sub) for sub in sub_map[root])
        
        return recur(id)
        
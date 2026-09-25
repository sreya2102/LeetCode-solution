"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        queue=deque()
        queue.append(root)
        m=0
        while queue:
            for i in range(len(queue)):
                node=queue.popleft()
                if i==0:
                    m=m+1
                for i in node.children:
                    queue.append(i)
        return m
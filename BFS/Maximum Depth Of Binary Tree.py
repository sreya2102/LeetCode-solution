# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
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
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return m

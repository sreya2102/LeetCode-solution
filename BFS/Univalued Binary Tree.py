# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        queue=deque()
        queue.append(root)
        ans=set()
        while queue:
            for i in range(len(queue)):
                node=queue.popleft()
                ans.add(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        if len(ans)==1:
            return True
        else:
            return False
            
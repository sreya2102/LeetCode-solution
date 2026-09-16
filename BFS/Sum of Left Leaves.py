# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        queue=deque()
        queue.append(root)
        arr=[]
        while queue:
            for i in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    if node.left.left is None and node.left.right is None:
                        arr.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return sum(arr)
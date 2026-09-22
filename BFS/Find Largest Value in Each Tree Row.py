# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        queue=deque()
        queue.append(root)
        arr=[]
        while queue:
            ans=[]
            for i in range(len(queue)):
                node=queue.popleft()
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            arr.append(max(ans))
        return arr
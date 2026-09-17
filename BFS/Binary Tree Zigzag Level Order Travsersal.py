# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        queue=deque()
        queue.append(root)
        brr=[]
        m=0
        while queue:
            arr=[]
            m=m+1
            for i in range(len(queue)):
                node=queue.popleft()
                arr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if m%2==0:
                arr.reverse()
            brr.append(arr)
        return brr
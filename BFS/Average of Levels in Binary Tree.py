# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
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
            a=(sum(ans))/len(ans)
            arr.append(a)
        return arr

                
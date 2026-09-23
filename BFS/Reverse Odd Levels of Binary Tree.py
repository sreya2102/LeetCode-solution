# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        queue=deque()
        queue.append(root)
        c=0
        while queue:
            nodes=[]
            ans=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                nodes.append(node)
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if c%2==1:
                ans.reverse()
                for i in range(len(nodes)):
                    nodes[i].val=ans[i]
            c=c+1
        return root
                
            


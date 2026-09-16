class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        queue=deque()
        queue.append(root)
        while queue:
            prev = None
            for i in range(len(queue)):
                node=queue.popleft()
                if prev:
                    prev.next=node
                prev=node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            prev.next=None
        return root
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp=head
        c=0
        while temp:
            c=c+1
            temp=temp.next
        k=k%c
        for i in range(k):
            temp=head
            while temp.next.next:
                temp=temp.next
            last=temp.next
            last.next=head
            temp.next=None
            head=last
        return head

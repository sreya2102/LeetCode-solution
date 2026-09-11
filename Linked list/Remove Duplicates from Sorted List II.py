# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        prev=None
        while temp:
            if temp.next is None or temp.val!=temp.next.val:
                prev=temp
                temp=temp.next
            else:
                value=temp.val
                while temp and temp.val==value:
                    temp=temp.next
                if prev:
                    prev.next=temp
                else:
                    head=temp
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        newEl = None
        while cur != None:
            newEl = ListNode(val=cur.val, next=newEl)
            cur = cur.next

        return newEl
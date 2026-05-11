# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Check for empty lists first
        if not list1: return list2
        if not list2: return list1
        
        cur1 = list1
        cur2 = list2
        newList = ListNode()
        newHead = newList
        while cur1 or cur2:
            if not cur2:
                newList.val = cur1.val
                newList.next = cur1.next
                break
            elif not cur1:
                newList.val = cur2.val
                newList.next = cur2.next
                break

            if cur1.val < cur2.val:
                newList.val = cur1.val
                cur1 = cur1.next
            else:
                newList.val = cur2.val
                cur2 = cur2.next
            
            newList.next = ListNode()
            newList = newList.next
        return newHead
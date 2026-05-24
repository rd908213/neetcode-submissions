# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3Head = ListNode()
        l3 = l3Head
        while l1 or l2:
            nodeSum = l3.val # Start out with the initial value in case remainder from previous additions
            if l1:
                nodeSum += l1.val
                l1 = l1.next
            
            if l2:
                nodeSum += l2.val
                l2 = l2.next

            print(f"CURRENT VALUE IS {nodeSum}")
            print(f"THIS NODE WILL HAVE VALUE {nodeSum % 10}")
            print(f"THE NEXT NODE WILL INITIALIZE WITH {int(nodeSum / 10)}")
            l3.val = nodeSum % 10 # Make sure only "ones" are included
            
            if (l1 or l2) or int(nodeSum / 10):
                l3.next = ListNode(val = int(nodeSum / 10)) # Initialize next node to have number of "tens"
                l3 = l3.next
            else:
                break
        return l3Head
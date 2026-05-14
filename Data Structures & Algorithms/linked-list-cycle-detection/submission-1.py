# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, visited=False):
        self.val = val
        self.next = next
        self.visited = visited

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        currNode=head
        if not currNode: # Edge empty case
            return False
        while currNode.next and not currNode.next.visited:
            print(f"node{currNode.val} -> node{currNode.next.val}")
            currNode.visited = True
            currNode = currNode.next
        if currNode.next == None:
            return False
        else:
            return True
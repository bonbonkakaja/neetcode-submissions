# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lookup = set()
        p = head
        while(p !=None):
            lookup.add(p)
            p = p.next
            if p in lookup:
                return True
        return False
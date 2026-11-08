# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s=[]
        ptr=head
        while(ptr!=None):
            s.append(ptr)
            ptr=ptr.next
        ptr=head
        tail = s[-1]
        while ptr!=None:
            n = ptr.next

            t =s.pop()

            if(ptr == t):
                ptr.next=None
                break
            if(n==t):
                ptr.next=t
                t.next=None
                break
            ptr.next=t
            t.next=n
            ptr=n
            




        
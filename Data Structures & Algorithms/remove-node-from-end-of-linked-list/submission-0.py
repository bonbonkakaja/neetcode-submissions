# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def getl(ptr):
    l=0
    while(ptr!=None):
        l+=1
        ptr=ptr.next
    return l
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = getl(head) # O(n)
        i=0
        ptr=head
        m = length -n 
        if(m==0):
            head=head.next
            return head
        while(ptr!=None):
            if(i==m-1):
                trm=ptr.next
                if(trm==None):

                    break
                else:
                    nptr=trm.next
                    ptr.next=nptr
                    ptr=nptr
                    break
            i+=1
            ptr=ptr.next
        return head

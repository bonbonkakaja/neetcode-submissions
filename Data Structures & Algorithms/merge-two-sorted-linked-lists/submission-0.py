# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def findminNode( list1: Optional[ListNode], list2: Optional[ListNode]):
    if(list1.val <= list2.val):
        return list1
    else:
        return list2

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        l1 = list1
        l2 = list2
        head = ListNode(0,None) 
        ptr= head
        while(l1!=None and l2!=None):

            mc=findminNode(l1,l2)
            ptr.next=mc
            if (mc == l1):
                l1=l1.next
            else:
                l2=l2.next
            ptr = ptr.next
        if (l1 !=None):
            ptr.next= l1
        else:
            ptr.next = l2
        return head.next
    


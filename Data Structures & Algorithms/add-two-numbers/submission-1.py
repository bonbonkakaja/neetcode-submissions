# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        ptr=head
        pre=None
        l=0
        while(ptr is not None):
            ptr=ptr.next
            l+=1
        return pre,l

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        _,len1=self.reverse(l1)
        _,len2=self.reverse(l2)
        res=None
        other=None
        if(len2>=len1):
            res=l2
            other=l1
        else:
            res=l1
            other=l2
        addi=0
        ptr1=res
        ptr2=other
        pre=None
        while(ptr2 is not None):
            num=addi+ptr1.val+ptr2.val
            val=num%10
            addi=num//10
            ptr1.val=val
            pre=ptr1
            ptr1=ptr1.next
            ptr2=ptr2.next
        if(addi==1 and ptr1!=None):
            while(ptr1 is not None):
                
                num=ptr1.val +1
                val=num%10
                addi=num//10
                ptr1.val=val
                pre=ptr1
                ptr1=ptr1.next
                
            
            
        if(addi==1 and ptr1==None):
            pre.next=ListNode(1,None)

            
        return res
        



        
        
        
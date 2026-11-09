"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

3 -> 
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ch=Node(0)
        ptr=head
        cptr=ch
        hashmap={}
        hashmap[None]=None
        while(ptr!=None):

            nN=Node(ptr.val)

            cptr.next=nN

            hashmap[ptr]=nN
            ptr=ptr.next
            
            cptr=cptr.next
        # second run
        ptr=head
        cptr=ch.next 
        while(ptr is not None and cptr is not None):
            r=ptr.random
            cptr.random = hashmap[r]
            ptr=ptr.next
            cptr=cptr.next



            
            


            

        return ch.next
            
            


class ListNode:
    def __init__(self, val=0, next=None,pre=None):
        self.val = val # key of the hashmap
        self.next = next
        self.pre = pre
class DoubleLinkedList:
    def __init__(self):
        self.length = 0
        self.head=None
        self.tail=None
    def remove(self,node: ListNode):
        # remove a given node in the dll -> gc will help us
        if (not node):
            print("NODE SHOULD NOT BE NONE, WHAT U TRY TO REMOVE??")
        if(node==self.head and node==self.tail):
            self.head=self.head.next
            self.tail=self.tail.pre
        elif(node==self.head):
            self.head=self.head.next

        elif(node==self.tail):
            self.tail=self.tail.pre
        else:
            #in the middle
            _pre=node.pre
            _next=node.next
            _pre.next=_next
            _next.pre=_pre
            
        self.length-=1
        

    def append(self,node: ListNode):
        #always add to the end of the dll

        if (self.tail):
            self.tail.next=node
            node.pre=self.tail
            self.tail=node
        else:
            self.tail=node
            self.head=node
        self.length+=1

    def print():
        #for debugging purpose ..
        pass
class LRUCache:

    #sync dll and hashmap state within get and put operation
    #make sure dll not exceed capacity

    def __init__(self, capacity: int):
        self.hashmap=dict()
        self.capacity=capacity
        self.ll= DoubleLinkedList()
        

    def get(self, key: int) -> int:
        res=-1
        if(key in self.hashmap):
            res,node=self.hashmap[key]
            self.ll.remove(node)
            self.ll.append(node)
        return res

        
        

    def put(self, key: int, value: int) -> None:
        if(key in self.hashmap):
            v,node=self.hashmap[key]
            self.hashmap[key]=(value,node)
            
            self.ll.remove(node)
            self.ll.append(node)

        else:
            if(self.ll.length>=self.capacity):
                #time to evict 
                lru_node=self.ll.head
                self.ll.remove(lru_node)
                self.hashmap.pop(lru_node.val, None)
                cur=ListNode(key)
                self.hashmap[key]=(value,cur)
                self.ll.append(cur)
            else:
                cur=ListNode(key)
                self.hashmap[key]=(value,cur)
                self.ll.append(cur)
        

class Node:
    def __init__(self,char=None,children=None,has_end=None):
        # children is a hashmap where key is the char? 
        self.char=char
        self.children=children
        self.has_end=has_end
    def __str__(self):
        return f"char {self.char} \n children {self.children} \n has_end {self.has_end}"


class PrefixTree:

    def __init__(self):
        self.head=Node(None,{},False)        

    def insert(self, word: str) -> None:
        cur=self.head
        last=False
        for inx,char in enumerate(word):
            search_list=cur.children
            if char in search_list:
                cur=search_list[char]
                # update has_end
                if(inx==len(word)-1):
                    cur.has_end=True
            else:
                if(inx==len(word)-1):
                    last=True
                search_list[char]=Node(char,{},last)

                #print(char,search_list[char])
                cur.children=search_list
                cur=search_list[char]
                
        



    def search(self, word: str) -> bool:
        cur=self.head
        for inx,char in enumerate(word):
            search_list=cur.children
            is_last=cur.has_end
            if(char in search_list):
                cur=search_list[char]
            else:
                return False
        return cur.has_end
        

                


        

    def startsWith(self, prefix: str) -> bool:
        cur=self.head
        for inx,char in enumerate(prefix):
            search_list=cur.children
            is_last=cur.has_end
            if(char in search_list):
                cur=search_list[char]
            else:
                return False
        return True
        

        
        
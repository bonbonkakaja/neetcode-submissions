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
    def insert_char(self,char,node) -> Node:

        search_list=node.children

        next=None
        if char in search_list:
            next=search_list[char]
        else:
            search_list[char]=Node(char,{},False)
            node.children=search_list
            next=search_list[char]
        return next
        
    def insert(self, word: str) -> None:
        cur=self.head
        for inx,char in enumerate(word):
            cur=self.insert_char(char,cur)


        cur.has_end=True
        


    def search(self, word: str) -> bool:

        def dfs(node,inx):
            if(node.has_end and inx==len(word)):
                return True
            elif(inx>=len(word)):
                return False

            sl=node.children
            if(word[inx] in sl):
                return dfs(sl[word[inx]],inx+1)
            elif(word[inx]=='.'):
                find=False
                for key in sl:
                    find=dfs(sl[key],inx+1)
                    if(find):
                        break
                return find
            else:
                return False
            
        return dfs(self.head,0)
        
        
class WordDictionary:

    def __init__(self):
        self.tree=PrefixTree()
        

    def addWord(self, word: str) -> None:
        self.tree.insert(word)
        
        

    def search(self, word: str) -> bool:
        return self.tree.search(word)
        

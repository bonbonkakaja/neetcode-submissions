def dict_cmp(leftmap,rightmap):
    for key in leftmap:
        if(not key in rightmap):
            return False
        if(rightmap[key]!=leftmap[key]):
            return False
    return True

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # make a hashmap out of s1
        refmap = {}
        for i in s1:
            refmap[i]=refmap.get(i,0)+1

        
        res=False
        wins=len(s1)

        hashmap ={}
         
        for left in range(len(s2)):
            right = left + wins
            if(right>len(s2)):
                break
            win= s2[left:right]
            for each in win:
                hashmap[each]=hashmap.get(each,0)+1
            if(dict_cmp(hashmap,refmap) and dict_cmp(refmap,hashmap)):
                return True
            
            for each in win:
                hashmap.pop(each,None)
        return False
                



        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left= 0
        right= 0
        if (len(s)==0):
            return 0
        hashmap = {s[0]:1}
        res  = 1
        while(left<=right and right+1 < len(s)):
            # print(hashmap)
            # print(left,right)
            
            # our goal is to find out that if the right we gonna expand is a duplicate to any element inside s[left:right+1]
            right +=1

            if s[right] not in hashmap:
                hashmap[s[right]]=0
            hashmap[s[right]]+=1
            if(s[right] in hashmap and (hashmap[s[right]]>1) ):
                # from left :right find the one that == right 
                while (left< right):
                    if (s[left]==s[right]):
                        hashmap[s[left]]-=1
                        left +=1
                        
                        break
                    else:
                        hashmap[s[left]]-=1
                        left +=1

            
            res = max(res,right-left+1)
                



        return res

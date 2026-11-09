class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left= 0
        right= 0
        res  = 0
        while(left<=right and right < len(s)):
            cur = len(set(s[left:right+1]))
            if(cur== len(s[left:right+1])):
                res = max(res,cur)
                right =right +1
            else:
                # from left :right find the one that == right 
                while (left< right):
                    if (s[left]==s[right]):
                        left +=1
                        break
                    else:
                        left +=1


        return res

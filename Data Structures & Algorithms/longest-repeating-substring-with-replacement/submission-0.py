def get_max_from_map(hashmap):
    max_value=0
    for key in hashmap:
        max_value = max(hashmap[key],max_value)
    return max_value
class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0 
        hashmap = {}
        for right in range(len(s)):
            
            char = s[right]
            hashmap[char] = hashmap.get(char, 0) + 1
            hashmax=get_max_from_map(hashmap)
            # print(l,right,hashmap)
            #check if adding right will flasify the window, if so move left until the window is valid
            while(right-l+1 - hashmax >k):
                l+=1
                char = s[l]
                hashmap[char] = hashmap.get(char, 0) -1
                hashmax=get_max_from_map(hashmap)
            res = max(res,right-l +1)
        return res




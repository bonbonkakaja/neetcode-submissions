class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str=""
        for astr in strs:
            encode_str+=f"{len(astr)}#"
            encode_str+=astr
        print(encode_str)
        return encode_str
    def decode(self, s: str) -> List[str]:
        i=0
        is_nb=1
        nb_str=""
        res = []
        while ( i<len(s)):
            # print(i)
            if s[i] !='#' and is_nb==1:
                nb_str += s[i]
                i+=1
            elif s[i] == '#':
                #Proceed to find the substr
                start=i+1
                end=i+1+int(nb_str)
                sub_str=s[start:end]
                res.append(sub_str)
                i=end
                #Reset the nb state
                is_nb=1
                nb_str=""
        return res

        
        
                



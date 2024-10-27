class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # hash_table={}
        # reverse_hash_table={}
        # n=len(s)
        # for i in range(n):
        #     if s[i] in hash_table:
        #         # if s[i] is already mapped and its value in hashmap is not matching current t[i]
        #         if hash_table[s[i]] != t[i]:
        #             return False
            
        #     else:
        #         # if t[i] is already mapped to something in s[i]
        #         if t[i] in reverse_hash_table:
        #             return False
        #         hash_table[s[i]]=t[i]
        #         reverse_hash_table[t[i]]=s[i]
        # return True

        if len(s) != len(t):
            return False
        mydict = {}
        myset = set()
        for i in range(len(s)):
            if s[i] not in mydict:
                if t[i] not in myset:
                    mydict[s[i]] = t[i]
                    myset.add(t[i])
                else:
                    return False
            if mydict[s[i]] != t[i]:
                return False
        return True

                


x=Solution()
s = "abcd"
t = "abab"
print(x.isIsomorphic(s,t))
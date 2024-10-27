from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # you can also use Counter here
        a=(Counter(s))
        b=(Counter(t))
        return a==b
        
        # hash_table1={}
        # for i in s:
        #     hash_table1[i] = hash_table1.get(i,0)+1
        
        # hash_table2={}
        # for i in t:
        #     hash_table2[i] = hash_table2.get(i,0)+1
        # return hash_table1 == hash_table2


        # hash_table={}
        # for i in s:
        #     hash_table[i] = hash_table.get(i,0)+1
        
        # for i in t:
        #     if i in hash_table:
        #         hash_table[i] = hash_table[i]-1
        #     else:
        #         return False
        
        # return True
x=Solution()
s = "anagram"
t = "nagaram"
print(x.isAnagram(s,t))
class Solution:
    def reverseWords(self, s: str) -> str:
        n=len(s)-1
        current_word=""
        s_array=[]
        i=0
        while n>=0:
            if s[n].isalnum():
                current_word =  s[n] + current_word 
                # print(current_word)
            else:
                if current_word:
                    s_array.append(current_word)
                    current_word=''
            n-=1
        if current_word:
            s_array.append(current_word)
        
        # print(s_array)
        
        ans =""
        for i in s_array:
            ans += i + " "
        return ans[0:-1]
                


x=Solution()
s = "  hello world  "
a=x.reverseWords(s=s)
print(a)
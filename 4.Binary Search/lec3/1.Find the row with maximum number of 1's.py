class Solution:
    def rowMaxNoOf1s(self,matrix):
        n=len(matrix)
        maxCount=0
        index=-1

        for i in range(n):
            count=sum(matrix[i])
            if count>maxCount:
                maxCount=count
                index=i
            count=0
        return index


matrix=[[1, 1, 1], [0, 0, 1], [0, 0, 0]]
a=Solution()
print(a.rowMaxNoOf1s(matrix=matrix))
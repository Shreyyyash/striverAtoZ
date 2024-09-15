# rotate the image by 90 degrees (clockwise)

def rotate(matrix):
    n = len(matrix)
    # transposing the matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # reversing each row of the matrix
    for i in range(n):
        matrix[i].reverse()

    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))

# with using extra space
# ans=[]
#     final=[]
#     rows=len(matrix)
#     cols=len(matrix[0])
    
#     for i in range(rows):
#         for j in range(cols-1,-1,-1):
#             ans.append(matrix[j][i])
#         final.append(ans)
#         ans=[]
        
#     print(final)
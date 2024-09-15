def setZeroes(matrix):
    rows = len(matrix)
    cols= len(matrix[0])
    r=[]
    c=[]
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col]==0:
                r.append(row)
                c.append(col)   
    for i in r:
        for j in range(cols):
            matrix[i][j]=0
    
    for j in c:
        for i in range(rows):
            matrix[i][j]=0
    
    return matrix
    
    print(r,c)


# matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix = [[1,1,1],[1,0,1],[1,1,1]]
a=setZeroes(matrix)
print(a)

# hash_map={}
#     rows = len(matrix)
#     cols= len(matrix[0])
    
#     for row in range(rows):
#         for col in range(cols):
#             if matrix[row][col]==0:
#                 hash_map[row,col]=True
    
#     for (i, j) in hash_map.keys():
#         for col in range(cols):
#             matrix[i][col]=0
#         for row in range(rows):
#             matrix[row][j]=0
    
#     return matrix
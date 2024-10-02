def generate(numRows):
    triangle=[]
    
    for i in range(numRows):
        row = [1]
        if i > 0:
            last_row = triangle[i - 1]
            for j in range(1,len(last_row)):
                row.append(last_row[j - 1] + last_row[j])
            row.append(1)
        triangle.append(row)
    
    return triangle

print(generate(5))
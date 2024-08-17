def selectionSort(array,size):
    for i in range(size):
        min_index=i
        for j in range(i+1,size):
            if array[j]<array[min_index]:
                min_index=j
        array[min_index],array[i]=array[i],array[min_index]
        # print(array)
    return array

array=[5,4,9,2,3,1]
n=len(array)
a=selectionSort(array,n)
print(a)

# https://www.geeksforgeeks.org/selection-sort/
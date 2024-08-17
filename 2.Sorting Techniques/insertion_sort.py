def insertionSort(array,size):
    for i in range(1,size):
        j=i
        # print(j)
        while j>0 and array[j-1]>array[j]:
            array[j],array[j-1]=array[j-1],array[j]
            j-=1
            # print(f'inner {j}')
            # print(array)
    return array

arr=[5,4,9,2,3,1]
n=len(arr)
a=insertionSort(arr,n)
print(a)

# https://www.geeksforgeeks.org/insertion-sort/
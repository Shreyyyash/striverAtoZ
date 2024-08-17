def bubbleSort(array,size):
    for i in range(size):
        isSorted=True
        for j in range(size-1-i):
            if array[j]>array[j+1]:
                isSorted=False
                array[j],array[j+1]=array[j+1],array[j]
                       
        if isSorted==True:
            # no swap happend means array is sorted no need to sort again
            break
        # print(array)
    return array

array=[5,4,9,2,3,1]
n=len(array)
a=bubbleSort(array,n)
print(a)
# optimization : if array is sorted no need to sort again

# https://www.geeksforgeeks.org/bubble-sort/
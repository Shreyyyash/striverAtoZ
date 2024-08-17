def smallest(array):
    n=len(array)
    min=array[0]
    for i in range(n):
        if array[i]<min:
            min=array[i]
    print(min)

array=[3,7,4,5,9,2,10,1]
smallest(array)